from django.test import TestCase
from .models import Menu, Booking, UserComments

class TestMenuModel(TestCase):
    def test_menu_model(self):
        menu_item = Menu.objects.create(
            name='Cheeseburger',
            price=8.99,
            category='Burgers'
        )
        self.assertEqual(str(menu_item), 'Cheeseburger')  # Customize based on your model's __str__ method

        # Add more tests for other model fields and methods as needed

class TestBookingModel(TestCase):
    def test_booking_model(self):
        booking = Booking.objects.create(
            # Add relevant fields for the Booking model
        )
        self.assertIsNotNone(booking.id)  # Ensure the model instance has an ID after creation

        # Add more tests for other model fields and methods as needed

class TestUserCommentsModel(TestCase):
    def test_user_comments_model(self):
        user_comment = UserComments.objects.create(
            first_name='John',
            last_name='Doe',
            comment='Great food!'
        )
        self.assertEqual(str(user_comment), 'John Doe: Great food!')  # Customize based on your model's __str__ method

        # Add more tests for other model fields and methods as needed
