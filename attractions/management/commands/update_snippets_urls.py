from django.core.management.base import BaseCommand
from attractions.models import Attractions


class Command(BaseCommand):
    help = 'Update Google Maps URLs for all attractions'

    def handle(self, *args, **kwargs):
        attractions = Attractions.objects.all()
        for attraction in attractions:
            base_url = "https://www.google.com/maps/search/?api=1&query="
            query = f"{attraction.title},{attraction.city},{attraction.country}"
            attraction.url = base_url + query.replace(" ", "+")
            attraction.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated URL for {attraction.title}'))
            print(attraction.url)