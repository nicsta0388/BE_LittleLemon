from django.urls import path, include
from restaurant.views import *
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers



# router = routers.DefaultRouter()
# router.register("booking", BookingViewSet)
# router.register("menu-items", MenuItemsView, basename="Menu_Items")

urlpatterns = [
    path('', views.index, name='index'), 
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
]

