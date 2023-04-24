from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import ReminderForm
from .tasks import send_email


def sender(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)

        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            text_reminder = form.cleaned_data['text_reminder']
            date_to_remind = form.cleaned_data['date_to_remind']
            current_time = timezone.now()

            if date_to_remind - current_time < timedelta(days=2):
                send_email.apply_async(args=(to_email, text_reminder), eta=date_to_remind)

                return redirect('celery_email:success')

            else:
                return HttpResponse(form.errors['date_to_remind'].as_data())

    else:
        form = ReminderForm()

    return render(request, 'celery_email/reminder.html', {'form': form})


def success(request):
    return render(request, 'celery_email/success.html')
