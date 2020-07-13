from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    domain = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    added_date = models.DateTimeField(default=timezone.now)

    def add(self):
        #self.published_date = timezone.now()
        self.added_date = timezone.now()

        self.save()

    def __str__(self):
        return self.title


