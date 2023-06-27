from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('properties/<str:location>/', views.get_properties_by_location, name='get_properties_by_location'),
    path('property/<int:property_id>/', views.get_property_details, name='get_property_details'),
    path('user/<int:user_id>/', views.get_user_profile, name='get_user_profile'),
    path('add-listing/', views.AddListing.as_view(), name='add_listing'),
]
