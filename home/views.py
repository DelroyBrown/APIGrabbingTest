# Import the required functions from Django's short cuts and http modules
from django.shortcuts import render
from django.http import JsonResponse
# Import the ChallengeAPI model from the current app's models
from .models import ChallengeAPI


# Define a view for retrieving all the data from the ChallengeAPI model
def retrieve_data(request):
    # Get all the data from the ChallengeAPI model
    data = ChallengeAPI.objects.all()

    # Initialize an empty list to store the data
    data_list = []

    # Loop through the data queryset and append each item's information as a dictionary
    for item in data:
        data_list.append({
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'quantity': item.quantity,
        })

    # Store the data_list in a context dictionary
    context = {'data': data_list}

    # Render the home.html template and pass the context dictionary to it
    return render(request, 'home.html', context)


# Define a view for displaying the detail of a specific item
def detail(request, pk):
    # Get the item from the ChallengeAPI model based on the primary key (pk)
    item = ChallengeAPI.objects.get(pk=pk)

    # Store the item's information in a context dictionary
    context = {
        'id': item.id,
        'name': item.name,
        'price': float(item.price),
        'quantity': item.quantity,
    }

    # Render the detail.html template and pass the context dictionary to it
    return render(request, 'detail.html', context)


# Define a view for searching the data
def search(request):
    # Get the value of the query parameter 'q' from the GET request
    q = request.GET.get('q')

    # If the 'q' parameter exists in the GET request
    if q:
        # Get the data from the ChallengeAPI model that contains the 'q' value in its id field
        data = ChallengeAPI.objects.filter(id__icontains=q)
    else:
        # If the 'q' parameter does not exist, get all the data from the ChallengeAPI model
        data = ChallengeAPI.objects.all()

    # Initialize an empty list to store the data
    data_list = []

    # Loop through the data queryset and append each item's information as a dictionary
    for item in data:
        data_list.append({
            'id': item.id,
            'name': item.name,
            'price': float(item.price),
            'quantity': item.quantity,
        })

    # Render the retrieve_data.html template and pass the data_list stored in a context dictionary to it
    return render(request, 'retrieve_data.html', {'data': data_list})
