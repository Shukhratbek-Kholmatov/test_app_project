import os
from urllib import request
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        Profile.objects.create(user=user)
    



