from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def send_activation_email_task(subject, message, recipient_list, html_message):
    for recipient in recipient_list:
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], html_message=html_message)
    return f"Emails sent to {', '.join(recipient_list)}."


@shared_task
def delete_cache_task(cache_key):
    cache.delete(cache_key)
    print(f"Cache key {cache_key} successfully deleted.")
    return f"Cache key {cache_key} successfully deleted."




