from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from core.models import Property

def get_properties_by_location(request, location):
    # Retrieve properties based on the specified location
    properties = Property.objects.filter(location=location)
    
    # Create a list to store the property data
    property_list = []
    
    # Iterate over the properties and extract the necessary data
    for property in properties:
        property_data = {
            'id': property.id,
            'title': property.title,
            'description': property.description,
            # Add more fields as needed
        }
        property_list.append(property_data)
    
    # Create a dictionary with the property list
    data = {
        'properties': property_list
    }
    
    # Return the JSON response
    return JsonResponse(data)

class AddListing(View):
    def get(self, request):
        # Render the template for the add listing form
        return render(request, 'api/add_listing.html')

    def post(self, request):
        # Handle POST request logic here
        # Extract the necessary data from the request
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        city = request.POST.get('city')
        category = request.POST.get('category')

        # Create a new Property object with the extracted data
        property = Property(
            title=title,
            description=description,
            price=price,
            city=city,
            category=category
        )

        # Save the Property object
        property.save()

        # Return the appropriate response
        return JsonResponse({'message': 'Property listing created successfully'})