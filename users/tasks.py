# users/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

@shared_task
def send_like_notification(user_id, recipe_name):
    user = get_user_model().objects.get(pk=user_id)
    subject = f'Your recipe "{recipe_name}" received a like!'
    message = f'Congratulations! Your recipe "{recipe_name}" received a like from our users.'
    recipient_list = [user.email]
    send_mail(subject, message, None, recipient_list)
