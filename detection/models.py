from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
# Create your models here.


fs = FileSystemStorage(location='media')
# Create your models here.
class Image(models.Model):
    image = models.ImageField(storage=fs)
    path = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='new_image')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.path