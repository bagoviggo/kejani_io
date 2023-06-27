from django.urls import path
from .views import HomeView
from api.views import AddListing

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-listing/', AddListing.as_view(), name='add-listing'),
]
