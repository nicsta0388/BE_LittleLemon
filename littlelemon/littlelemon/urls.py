"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from restaurant import views
from restaurant.views import BookingViewSet,MenuItemsView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register("booking", views.BookingViewSet)
router.register("menu-items", views.MenuItemsView, basename="Menu_Items")

# from django.conf import settings
# from django.conf.urls.static import static

# Create a router and register your viewset with it.
#router = DefaultRouter()
#router.register(r'restaurant', views.BookingViewSet)

# router = DefaultRouter(trailing_slash=False)
# router.register('tables', views.BookingViewSet.as_view({'get': 'retrieve'}), basename="Booking")
api_patterns =  [
    path("message/", views.msg),
    path("api-token-auth/", obtain_auth_token),
]

auth_patterns =  [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("api/", include(api_patterns)),
    path("auth/", include(auth_patterns)),
    path('routers/', include(router.urls)),

]

