from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Guest.objects.create(user=instance)
        Guest.name = instance.username
        Guest.email = instance.email
        print('profile created!')
        
#post_save.connect(create_profile, sender=User) 

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.guest.save()
        print('Profile update!')
        
#post_save.connect(create_profile, sender = User) 
