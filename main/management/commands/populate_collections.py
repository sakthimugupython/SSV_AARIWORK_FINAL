from django.core.management.base import BaseCommand
from main.models import HeroSection, Collection, Arrival, AcademySection

class Command(BaseCommand):
    help = 'Populate collections page with sample data'

    def handle(self, *args, **options):
        # Create or update hero section for collections page
        hero, created = HeroSection.objects.get_or_create(
            title="Our Collections",
            defaults={
                'subtitle': 'Discover our curated selection of exquisite AARI embroidery designs',
                'primary_button_text': 'Explore Collections',
                'primary_button_url': '/collections/',
                'secondary_button_text': 'Get Quote',
                'secondary_button_url': '/contact/',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created hero section: {hero.title}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated hero section: {hero.title}'))

        # Create sample collections
        collections_data = [
            {
                'name': 'Traditional Collection',
                'description': 'Classic AARI designs that showcase the timeless beauty of traditional embroidery techniques passed down through generations.',
                'button_text': 'View Collection',
                'button_url': '#traditional',
                'order': 1
            },
            {
                'name': 'Contemporary Collection',
                'description': 'Modern interpretations of AARI work that blend traditional craftsmanship with contemporary aesthetics and innovative designs.',
                'button_text': 'View Collection',
                'button_url': '#contemporary',
                'order': 2
            },
            {
                'name': 'Bridal Collection',
                'description': 'Elegant bridal wear featuring intricate AARI embroidery perfect for special occasions and creating lasting memories.',
                'button_text': 'View Collection',
                'button_url': '#bridal',
                'order': 3
            }
        ]

        for collection_data in collections_data:
            collection, created = Collection.objects.get_or_create(
                name=collection_data['name'],
                defaults=collection_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created collection: {collection.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated collection: {collection.name}'))

        # Create sample arrivals (featured items)
        arrivals_data = [
            {
                'name': 'Royal Heritage Saree',
                'description': 'Exquisite AARI work featuring traditional motifs and premium silk fabric.',
                'price': 15000.00,
                'button_text': 'Enquiry Now',
                'order': 1
            },
            {
                'name': 'Modern Art Blouse',
                'description': 'Contemporary design with traditional AARI techniques on premium cotton.',
                'price': 8500.00,
                'button_text': 'Enquiry Now',
                'order': 2
            },
            {
                'name': 'Designer Lehenga',
                'description': 'Stunning bridal wear with intricate AARI embroidery and luxurious fabric.',
                'price': 25000.00,
                'button_text': 'Enquiry Now',
                'order': 3
            },
            {
                'name': 'Classic Kurti Set',
                'description': 'Beautiful everyday wear enhanced with delicate AARI work.',
                'price': 12000.00,
                'button_text': 'Enquiry Now',
                'order': 4
            }
        ]

        for arrival_data in arrivals_data:
            arrival, created = Arrival.objects.get_or_create(
                name=arrival_data['name'],
                defaults=arrival_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created arrival: {arrival.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated arrival: {arrival.name}'))

        # Create or update academy section
        academy, created = AcademySection.objects.get_or_create(
            title="Learn AARI Embroidery",
            defaults={
                'description': 'Master the art of AARI embroidery through our hands-on workshops and training sessions with expert artisans.',
                'button_text': 'Explore Academy',
                'button_url': '/ssv-academy/',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created academy section: {academy.title}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated academy section: {academy.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated collections page with sample data!'))
