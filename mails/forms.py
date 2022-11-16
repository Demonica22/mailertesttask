from django.contrib.auth.forms import forms
from users.models import User
from .models import Mail


class MailComposeForm(forms.ModelForm):
    receivers = forms.MultipleChoiceField(choices=[(elem.id, elem.email) for elem in User.objects.all()])

    class Meta:
        model = Mail
        fields = ('receivers', 'title', 'text')
