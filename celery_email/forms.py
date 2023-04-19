from django import forms


class ReminderForm(forms.Form):
    to_email = forms.EmailField()
    text_reminder = forms.CharField(max_length=200, widget=forms.Textarea)
    date_to_remind = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
