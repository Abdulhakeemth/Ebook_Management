from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
Genre_status =(
        ('Fantasy', 'fantasy'),
        ('Literary', 'literary'),
        ('Mystery', 'mystery'),
        ('Non-Fiction','non-fiction'),
        ('Science Fiction','science fiction'),
        ('Thriller','thriller')
        )
class Ebooks(models.Model):
    Title=models.CharField(max_length=20)
    Author=models.CharField(max_length=20)
    Genre=models.CharField(choices=Genre_status,max_length=15)
#     Review=models.FloatField()
    Favorite=models.BooleanField(default=True)

class Rating(models.Model):
        User=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User',blank=True,null=True)
        Book=models.ForeignKey(Ebooks,on_delete=models.CASCADE,related_name='Ebooks',blank=True,null=True)
        Review=models.FloatField()