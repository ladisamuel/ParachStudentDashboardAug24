from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets
import random
# from django.contrib.auth.models import User


# class CustomUser(AbstractUser):
class CustomUser(models.Model):
    # pass
    user_type_data = (
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('User', 'User'),
    )
    user_type = models.CharField(choices=user_type_data, default=user_type_data[-1], max_length=200)

    # user_trial = models.BooleanField(default=True)
    # user_disallowed = models.BooleanField(default=False)
    


    def P_key(self):
        key = ''
        # pass
        character = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#+@%&_-')
        length = 5
        k_ads = ''

        for x in range(length):
            k_ads += random.choice(character)
    
        # key = ''
        while not self.key:
            key = 'xtrum_' + str(self.id) + secrets.token_urlsafe(10)+ k_ads + '=lis'
            # check_key = CustomUser.objects.filter(key=key)
            
            if CustomUser.objects.filter(P_key=key).exists():
            # if key in check_key:
                new_key = 'xtrum_' + str(self.id) + secrets.token_urlsafe(10)+ k_ads + '=lis'
                key = new_key
        print("from the model \n\n", key)
        return str(key)


            # object_with_similar_key = StudentPayment.objects.filter(ref=ref)

    def __str__(self):
        return f'{self.id} - {self.username}' 