from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


fs = FileSystemStorage(location='media')
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(storage=fs)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    link = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='news_posts')
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title