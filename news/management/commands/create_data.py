"""Command File."""

from django.core.management.base import BaseCommand
from news.models import Author, News
import requests

class Command(BaseCommand):
    """Command."""

    help = 'Populates the database with APi data.'

    def handle(self, *args, **options):
        """For Saving Data."""
        self.stdout.write(self.style.SUCCESS('Started database population process...'))
        response = requests.get(
            url="https://saurav.tech/NewsAPI/top-headlines/category/health/in.json").json()
        for data in response.get('articles'):
            author,_ = Author.objects.get_or_create(name=data.get("author") if data.get("author") is not None  
                        else "default author")
            News.objects.create(
                title=data.get("title") if data.get("title") else "default",
                short_description=data.get("description") if data.get("description") else "default",
                url=data.get("url"),
                author=author,
                content=data.get("content") if data.get("content") else "default",
            )
        self.stdout.write(self.style.SUCCESS('Data Saved Sucessfully.'))

        
