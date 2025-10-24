from django.core.management.base import BaseCommand
from main.models import ContactHeroSection

class Command(BaseCommand):
    help = 'Creates a default ContactHeroSection entry for the contact page banner'

    def handle(self, *args, **options):
        # Check if a ContactHeroSection already exists
        if ContactHeroSection.objects.exists():
            self.stdout.write(
                self.style.SUCCESS('ContactHeroSection already exists')
            )
            return

        # Create default ContactHeroSection
        contact_hero = ContactHeroSection.objects.create(
            title="Contact Us",
            subtitle="Get in touch with us for inquiries, custom orders, or workshop registrations",
            is_active=True
        )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created ContactHeroSection: {contact_hero.title}')
        )
