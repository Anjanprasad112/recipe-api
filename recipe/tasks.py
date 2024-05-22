# recipe/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Recipe

@shared_task
def send_daily_like_notification():
    # Retrieve all authors who have recipes with likes
    authors_with_likes = Recipe.objects.filter(likes__isnull=False).values_list('author', flat=True).distinct()

    for author_id in authors_with_likes:
        user = get_user_model().objects.get(pk=author_id)
        recipe_names = Recipe.objects.filter(author_id=author_id, likes__isnull=False).values_list('name', flat=True)
        
        subject = 'Daily Like Notifications'
        message = f'Hello {user.username},\n\n'
        message += 'Here are the likes received on your recipes today:\n'
        for recipe_name in recipe_names:
            message += f'- {recipe_name}\n'
        message += '\nKeep cooking and sharing amazing recipes!\n\nBest regards,\nThe Recipe Team'

        send_mail(subject, message, None, [user.email])
