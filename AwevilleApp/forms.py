from django.forms import ModelForm
from .models import Message, Booking, Room, Subscriber

class ContactForm(ModelForm):
    """
    A class based form for capturing data and storing in the database
    """

    class Meta:
        model = Message
        fields = "__all__"


class BookingForm(ModelForm):
    """
    A class based form for capturing data and storing in the database
    """

    class Meta:
        model = Booking
        fields = "__all__"
        

class SubscriberForm(ModelForm):
    """
    A class based form for capturing data and storing in the database
    """

    class Meta:
        model = Subscriber
        fields = "__all__"