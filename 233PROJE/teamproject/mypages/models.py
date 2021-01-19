from django.db import models


class Posts (models.Model):
    title= models.CharField(max_length=200)
    author=models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )
    body=models.TextField()

    def __str__(self):
        return self.title


class Messages(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30, unique=True)
    phone=models.CharField(max_length=15)
    yourmessage=models.CharField(max_length=300)
    
    def __str__(self):
        return "Name: "+ self.name + " Email: " + self.email + " Phone: " + self.phone + " Message: " + self.yourmessage


class FormName(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text









