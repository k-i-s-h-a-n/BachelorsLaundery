from django.db import models

# Create our models here.

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField(max_length=1678795,null=True)
    date=models.DateField()

    def __str__(self):
        return self.name
    
