from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=900)
    content = models.CharField(max_length=10000)
    category = models.CharField(max_length=45)
    publication_date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogpost_images', null=True, blank=True)

class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    githubaccount = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f"Nombre: {self.name} - Apellido: {self.lastname} - Email: {self.email} - Github: {self.githubaccount}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    message = models.CharField(max_length=700)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.user} - {self.imagen}"