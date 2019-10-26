from django.db.models.signals import post_save
from django.dispatch import Signal
from django.dispatch import receiver
from .models import CustomUser
from social_django.models import UserSocialAuth
# for reciever functions:
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
import json


User = get_user_model()


# NOTE: All created signals have to be imported in apps.py !



### SIGNALS ###
new_user_activation = Signal()                              # you can provide extra args -> providing_args=["example_data"]


### recievers ###
@receiver(new_user_activation)
def welcome_new_user(sender, **kwargs):
    new_user = sender
    print('================')
    print('New user registration!')
    print('method: basic auth')
    print(new_user.last_name, new_user.first_name)
    print(new_user.email)
    subject = '🎉 Köszönjük, hogy regisztráltál!'
    message = render_to_string('email/welcome_new_user.html', {
        'new_user': new_user,
    })
    to_email = new_user.email
    email = EmailMessage(
                subject, message, to=[to_email]
    )
    email.content_subtype = "html"          # important addition for html email to render !
    email.send()
    print('greeting email: sent >>>')
    print('================')




@receiver(post_save, sender = CustomUser)
def welcome_new_social_user(sender, instance, created, **kwargs):
    if created:
        if instance.is_active:
            new_user = instance
            print('=========================')
            print('New user registration!')
            print('method: social auth')
            print(new_user.email)
            subject = '🎉 Köszönjük, hogy regisztráltál!'
            message = render_to_string('email/welcome_new_user.html', {
                'new_user': new_user,
            })
            to_email = 'nyitrai.bence4@gmail.com'             # REPLACE THIS !
            email = EmailMessage(
                        subject, message, to=[to_email]
            )
            email.content_subtype = "html"          # important addition for html email to render !
            email.send()
            print('greeting email: sent >>>')
            print('=========================')