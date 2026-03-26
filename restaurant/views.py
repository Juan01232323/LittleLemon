from django.shortcuts import render
from .models import Menu, Booking  
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets 
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core import serializers
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    
def about(request):
    return render(request, 'about.html')


@csrf_exempt 
def book(request):
    if request.method == 'POST':
        data = json.load(request) # Lee el JSON del script
        booking = Booking(
            first_name=data['first_name'],
            reservation_date=data['reservation_date'],
            reservation_slot=data['reservation_slot'],
        )
        booking.save()
    return render(request, 'book.html')


def bookings(request):
    date = request.GET.get('date')

    if date:
        bookings_data = Booking.objects.filter(booking_date=date)
        data = list(bookings_data.values())
        return JsonResponse(data, safe=False)
    else:
        bookings_data = Booking.objects.all()
        data = list(bookings_data.values())

        json_data = json.dumps(data)

    return render(request, 'bookings.html', {
    "bookings": json.dumps(data)
})

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 