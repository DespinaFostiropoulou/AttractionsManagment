from django.db import models

CATEGORY_CHOICES = [
    ('historical', 'Historical'),
    ('cultural', 'Cultural'),
    ('natural', 'Natural'),
    ('religious', 'Religious'),
    ('entertainment', 'Entertainment')
]

owner = models.ForeignKey('auth.User', related_name='attractions', on_delete=models.CASCADE, null=True)


class Attractions(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='attractions/covers/')
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    linenos = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='attractions', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created']
