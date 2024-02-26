from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
# @receiver(post_save,sender=Profile)  
# def profileUpdated(sender,instance,created,**kwargs):
#     print('Profile Saved!')
#     print('Instance:',instance)
#     print('Created:',created)
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    print("hello............")
    if created:
      profile=  Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name,
        )

def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    
# post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=Profile)