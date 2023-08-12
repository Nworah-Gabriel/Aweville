from django.shortcuts import render

#---FUNCTIONAL VIEWS---#
def indexView(request):
    """
    A functional view for the home page (index.html)
    """
    return render(request, "index.html")


def teamView(request):
    """
    A functional view for the team page (team.html)
    """

    return render(request, "team.html")


def servicesView(request):
    """
    A functional view for the service page (service.html)
    """

    return render(request, "service.html")


def aboutView(request):
    """
    A functional based view for the about page (about.html)
    """

    return render(request, "about.html")


def bookingView(request):
    """
    A functional based view for the booking page (booking.html)
    """

    return render(request, "booking.html")


def roomView(request):
    """
    A functional based view for the rooms display (room.html)
    """

    return render(request, "rooms.html")


def contactView(request):
    """
    A functional based view for the contact page (contact.html)
    """

    return render(request, "contact.html")