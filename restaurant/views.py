from django.shortcuts import render
from .models import Menu, Booking  
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets 

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Maneja GET (listar) y POST (crear)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Maneja GET (detalle), PUT (actualizar) y DELETE (borrar)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # Nueva Vista de Reservas (ViewSet)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer