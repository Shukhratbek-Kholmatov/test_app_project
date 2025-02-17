from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Answer



# @receiver(post_save, sender=Answer)
# def create_profile(sender, instance, created, *args, **kwargs):
#     if instance.is_delete==True:
#         instance.delete()
        
    



