from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking
from django.urls import reverse
import datetime


class BookingModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password123')

    def test_booking_creation(self):
        """Check booking model string format"""
        booking = Booking.objects.create(
            user=self.user,
            full_name="Test User",
            email="test@example.com",
            phone="123456789",
            date=datetime.date.today(),
            time=datetime.time(10, 0),
            photoshoot_type="family",
        )
        expected_str = f"{
            self.user.username} - {
                booking.date} {booking.time} - {booking.photoshoot_type}"
        self.assertEqual(str(booking), expected_str)


class BookingViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='viewer', password='pass123')
        self.client.login(username='viewer', password='pass123')

    def test_booking_page_loads(self):
        """Ensure booking page loads for logged-in user"""
        response = self.client.get(reverse('book_photoshoot'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking.html')

    def test_booking_creation_via_post(self):
        """Test form submission creates booking"""
        response = self.client.post(reverse('book_photoshoot'), {
            'full_name': 'Client One',
            'email': 'client@example.com',
            'phone': '',
            'date': (
                datetime.date.today() + datetime.timedelta(
                    days=1)).isoformat(),
            'time': datetime.time(12, 0),
            'photoshoot_type': 'Events',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().full_name, "Client One")
