from django.db import models
from photologue.models import Gallery
# Create your models here.
class Post(models.Model):
 
    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True)
    
    title = models.CharField(max_length=199)
    content = models.TextField()
    
    slug = models.SlugField(max_length=250, allow_unicode=True, blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.title