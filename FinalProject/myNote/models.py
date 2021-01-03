from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=150)
    # note_pic = models.ImageField(upload_to='images/')
    # note_pic = models.FileField(upload_to='images/')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.id}-{self.name} - {self.added_on} - {self.updated_on}"
