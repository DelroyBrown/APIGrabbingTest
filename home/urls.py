from django.urls import path
from .views import retrieve_data, detail, search

urlpatterns = [
    path('data/', retrieve_data, name='retrieve_data'),
    path('data/<int:pk>/', detail, name='detail'),
    path('search/', search, name='search'),

]