from celery import shared_task
from copy import deepcopy
from .models import Mail
from users.models import User


@shared_task()
def create_mail(data):
    try:
        mail_piece = Mail()
        mail_piece.id = None
        mail_piece.receiver = User.objects.get(id=data['receiver'])
        mail_piece.sender = User.objects.get(id=data['sender'])
        mail_piece.text = data['text']
        mail_piece.title = data["title"]
        mail_piece.save()
    except Exception as x:
        print("Error in sending a message:\n", x)
