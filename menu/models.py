from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100) 
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'title {self.title}'
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})