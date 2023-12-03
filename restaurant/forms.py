from django import forms
from .models import UserComments
from .models import Booking

class CommentForm(forms.ModelForm):
    class Meta:
        model=UserComments
        fields='__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'