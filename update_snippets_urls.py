from django.core.management.base import BaseCommand
from attractions.models import Attractions


class Command(BaseCommand):
    help = 'Update Google Maps URLs for all attractions'

    def handle(self, *args, **kwargs):
        attractions = Attractions.objects.all()
        for attractions in attractions:
            base_url = "https://www.google.com/maps/search/?api=1&query="
            query = f"{attractions.title},{attractions.city},{attractions.country}"
            attractions.url = base_url + query.replace(" ", "+")
            attractions.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated URL for {attractions.title}'))