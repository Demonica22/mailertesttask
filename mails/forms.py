from django.contrib.auth.forms import forms
from users.models import User
from .models import Mail
from django.core.validators import MinValueValidator


class MailComposeForm(forms.ModelForm):
    receivers = forms.MultipleChoiceField(choices=[(elem.id, elem.email) for elem in User.objects.all()])
    time_to_send = forms.IntegerField(validators=[MinValueValidator(0)], initial=0,
                                      help_text="(seconds)")

    class Meta:
        model = Mail
        fields = ('receivers', 'title', 'text')
