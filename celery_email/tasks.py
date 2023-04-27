from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail as django_send_mail

import requests

from .models import Author, Quote


@shared_task
def send_email(text_reminder, to_email):
    django_send_mail(
        'Subject',
        text_reminder,
        'example@outlook.com',
        ['list@example.com'],
        to_email,
    )


@shared_task
def parse_quote():
    saved_quotes = 0
    page_no = 1
    while True:
        r = requests.get(f"https://quotes.toscrape.com/page/{page_no}/")
        soup = BeautifulSoup(r.text, 'html.parser')
        for quote in soup.findAll('div', {'class': 'quote'}):
            text = quote.find('span', {'class': 'text'}).string
            author_name = quote.find('small', {'class': 'author'}).string
            author_about = quote.find('small', {'class': 'author'}).find_next('a')['href']
            author_link = requests.get('https://quotes.toscrape.com' + author_about)
            author_soup = BeautifulSoup(author_link.text, 'html.parser')
            author_born_date = author_soup.find('span', {'class': 'author-born-date'}).string
            born_location = author_soup.find('span', {'class': 'author-born-location'}).string
            born = author_born_date + " " + born_location
            author, created = Author.objects.get_or_create(name=author_name, born=born)
            quote, created = Quote.objects.get_or_create(quote_text=text, author=author)
            if created:
                saved_quotes += 1
            if saved_quotes == 5:
                return
        next_page = soup.find('li', {'class': 'next'})
        if not next_page:
            send_email(
                'Parsed successfully!',
                'No new quotes found.',
                'admin@gmail.com',
                fail_silently=False,
                recipient_list=['ivanmuratov.2016@gmail.com']
            )
            break
        page_no += 1
