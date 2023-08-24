from django.shortcuts import render, HttpResponseRedirect 
from .forms import ContactForm, BookingForm, SubscriberForm
from .models import Room
from django.core.paginator import Paginator
from django.views.generic import DetailView
from .models import Booking


#---FUNCTIONAL VIEWS---#
def indexView(request):
    """
    A functional view for the home page (index.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()

    Rooms = Room.objects.all()
    paginator = Paginator(Rooms, 3)

    #---FOR DREAM ROOM PAGINATION---#
    paginator_page_number = request.GET.get("page")
    page_obj = paginator.get_page(paginator_page_number)
  

    return render(request, "index.html", { 'subscriberForm': subscriberForm, "Rooms": page_obj})


def teamView(request):
    """
    A functional view for the team page (team.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()

    return render(request, "team.html", { 'subscriberForm': subscriberForm })


def servicesView(request):
    """
    A functional view for the service page (service.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()

    return render(request, "service.html", { 'subscriberForm': subscriberForm })


def aboutView(request):
    """
    A functional based view for the about page (about.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()

    return render(request, "about.html", { 'subscriberForm': subscriberForm })


def bookingView(request):
    """
    A functional based view for the booking page (booking.html)
    """

    form = BookingForm(request.POST)
   
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("https:aweville.onrender.com/success")
    
    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            
    return render(request, "booking.html", {'form':form, 'subscriberForm': subscriberForm })


def SpecialBookingView(request, Title, value):
    """
    A functional based view for the special booking page (SpecialBooking.html)
    """

    form = BookingForm(request.POST)
   
    if request.method == 'POST':
        print("Posted")
        if form.is_valid():
            print("valid")
            form.save()

            Checkin = form.cleaned_data["CheckIn"]
            Checkout = form.cleaned_data["CheckOut"]

            query = Booking.objects.get(CheckIn=Checkin, CheckOut=Checkout)
            query.RoomTitle = Title
            query.save()
            return HttpResponseRedirect('https:aweville.onrender.com/success')
        
    
    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
            
    return render(request, "SpecialBooking.html", {'form':form, 'subscriberForm': subscriberForm, "title":Title, "url":value })


def roomView(request):
    """
    A functional based view for the rooms display (room.html)
    """

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()

    Rooms = Room.objects.all()
    paginator = Paginator(Rooms, 3)

    #---FOR DREAM ROOM PAGINATION---#
    paginator_page_number = request.GET.get("page")
    page_obj = paginator.get_page(paginator_page_number)

    for room in Rooms:
        print(room.id)        

    return render(request, "rooms.html", { 'subscriberForm': subscriberForm, "Rooms": page_obj})



def contactView(request):
    """
    A functional based view for the contact page (contact.html)
    """

    form = ContactForm(request.POST)
   
    if request.method == 'POST':
        print(form)
        if form.is_valid():
            form.save()

    # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
      
    return render(request, "contact.html", {'form':form, 'subscriberForm': subscriberForm })



def alertView(request):
    """
    A functional based view for the alert page (alert.html)
    """

     # ---FOR EMAIL SUBSCRIBING---#
    subscriberForm = SubscriberForm(request.POST)
   
    if request.method == 'POST':
        if subscriberForm.is_valid():
            subscriberForm.save()
    return render(request,  "alert.html", {'subscriberForm': subscriberForm })


class RoomImageDisplay(DetailView):

    model = Room
    template_name = 'room.html'
    context_object_name = 'room'