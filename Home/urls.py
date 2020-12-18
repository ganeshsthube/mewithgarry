from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.just, name = 'Home'),
    path("links", views.links, name = 'links'),
    path("contact",views.contact, name = 'contact'),
    path("Home",views.just, name = 'HomeD')
]