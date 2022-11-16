from django.db import models
from users.models import User
from django.urls import reverse


# Create your models here.
class Mail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")

    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000, blank=True, null=True)
    was_read = models.BooleanField(default=False)

    def __str__(self):
        mail_info = f"From: {self.sender}" \
                    f"To: {self.receiver}" \
                    f"Title: {self.title}" \
                    f"Text: {self.text}" \
                    f"Was read?: {self.was_read}"
        return mail_info

    def get_info(self):
        mail_info = [f"From: {self.sender}",
                     f"To: {self.receiver}",
                     f"Title: {self.title}",
                     f"Text: {self.text}",
                     f"Was read?: {self.was_read}"]
        return mail_info

    def get_absolute_url(self):
        return reverse('mails:detail', args=[self.id])
