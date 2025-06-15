from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **options):
        # Clear existing data
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

        # Create listings
        listings = [
            Listing.objects.create(
                title='Beachfront Villa',
                description='Luxury villa with ocean view',
                location='Malibu, CA',
                price_per_night=350.00
            ),
            Listing.objects.create(
                title='Downtown Apartment',
                description='Modern apartment in city center',
                location='New York, NY',
                price_per_night=200.00
            ),
            Listing.objects.create(
                title='Mountain Cabin',
                description='Cozy cabin with mountain views',
                location='Aspen, CO',
                price_per_night=150.00
            )
        ]

        # Create bookings
        today = datetime.now().date()
        for listing in listings:
            booking = Booking.objects.create(
                listing=listing,
                guest_name=f"Guest {random.randint(1, 100)}",
                check_in=today + timedelta(days=7),
                check_out=today + timedelta(days=14)
            )

            # Create reviews
            Review.objects.create(
                listing=listing,
                reviewer_name=f"Reviewer {random.randint(1, 100)}",
                comment="Great experience!",
                rating=random.randint(4, 5)
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))