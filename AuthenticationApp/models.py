from django.db import models

# Create your models here.

class Login(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserEmail = models.EmailField(verbose_name="email", max_length=320, unique=True, null=False)
    UserPasswordHash = models.CharField(max_length=256, verbose_name="pass")
