from django.contrib.auth.forms import forms
from users.models import User
from .models import Mail
from django.core.validators import MinValueValidator


class MailComposeForm(forms.ModelForm):
    receivers = forms.MultipleChoiceField(choices=[(elem.id, elem.email) for elem in User.objects.all()])
    # send_now = forms.BooleanField(initial=True)
    # date_to_send = forms.DateTimeField(widget=forms.DateTimeInput)
    time_to_send = forms.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        model = Mail
        fields = ('receivers', 'title', 'text')
