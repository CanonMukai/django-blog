from django.conf import settings
from django.db import models
from django.utils import timezone

# Another name is availavle.
# models.Model means that this object is Django Model.
class Post(models.Model):
    # ForeignKey is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
