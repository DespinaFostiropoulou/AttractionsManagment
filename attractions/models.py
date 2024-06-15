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
    urls = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.url:
            base_url = "https://www.google.com/maps/search/?api=1&query="
            query = f"{self.title}, {self.city}, {self.country}"
            self.url = base_url + query.replace("","+")
        super(Attractions, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']
