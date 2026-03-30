from django.shortcuts import render
from .models import Menu, Booking  
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework import generics, viewsets 
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.core import serializers  
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User


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
        data = json.loads(request.body) # Cambia json.load por json.loads(request.body)
        
        booking = Booking(
            first_name=data['first_name'],
            booking_date=data['reservation_date'], # 'reservation_date' del form va a 'booking_date' del modelo
            no_of_guests=data.get('no_of_guests', 1) # Si el form no tiene invitados, ponemos 1 por defecto
        )
        booking.save()
        return JsonResponse({"status": "success"}) # Es buena práctica retornar un JSON en un POST de este tipo
        
    return render(request, 'book.html')


from django.core.serializers.json import DjangoJSONEncoder
import json

def bookings(request):
    date = request.GET.get('date')

    if date:
        bookings_data = Booking.objects.filter(booking_date=date)
        data = list(bookings_data.values())
        # Usamos el codificador de Django aquí para que no falle con las fechas
        return JsonResponse(data, safe=False, encoder=DjangoJSONEncoder)
    else:
        bookings_data = Booking.objects.all()
        data = list(bookings_data.values())
        json_data = json.dumps(data, cls=DjangoJSONEncoder)

    return render(request, 'bookings.html', {"bookings": json_data})


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

class VistaUsuarios(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
