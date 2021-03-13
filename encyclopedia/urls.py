from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path('search/', views.search, name='search'),
    path('new/', views.newPage, name='new'),
    path('newPage', views.createNewPage, name='newPage'),
    path('random/', views.randomPage, name='random'),
    path('edit/', views.edit, name='edit'),
    path('save/', views.save, name='save'), 
    path("wiki/<str:title>", views.entry, name="title")
]
