from django.contrib import admin
from .models import Attractions


admin.site.register(Attractions)
list_display = ('title', 'category', 'country', 'city', 'created')
search_fields = ('title', 'category', 'country', 'city')
list_filter = ('category', 'country', 'city')
