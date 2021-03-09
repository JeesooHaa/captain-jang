from django.db import models


class Letter(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ('-pk', )
