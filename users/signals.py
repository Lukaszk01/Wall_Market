from django.db.models.signals import post_saved
from django.contrib.auth.models import User
from django.dispatch import reciver
from .models import Profile

@reciver(post_save, sender=User)
def create_profile(sender, instance, created, **kawrgs):
  if created:
    Profile.object.create(user=instance)

@reciver(post_save, sender=User)
def save_profile(sender, instance, **kawrgs):
  instance.profile.save()
