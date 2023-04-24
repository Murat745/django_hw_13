from django.contrib import admin

from .models import Author, Quote


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'born']
    search_fields = ['name']


@admin.register(Quote)
class QuoteModelAdmin(admin.ModelAdmin):
    list_display = ['quote_text', 'author']
    raw_id_fields = ('author',)
