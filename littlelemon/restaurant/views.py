from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

from .models import Menu, Booking, Employees

from .serializers import MenuSerializer, BookingSerializer, UserSerializer, MenuItemSerializer

from django.contrib.auth.models import User


# Create your views here.

# def sayHello(request):
#  return HttpResponse('Hello World')



def index(request):
    return render(request, 'index.html', {})



class MenuItemsView(viewsets.ModelViewSet, generics.RetrieveUpdateAPIView, generics.DestroyAPIView): # , generics.ListCreateAPIView, generics.DestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class UserViewSet(viewsets.ModelViewSet,generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
   #permission_classes = [IsAuthenticated]
   queryset = User.objects.all()
   serializer_class = UserSerializer
   

class BookingViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@csrf_exempt  
@api_view()
@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})