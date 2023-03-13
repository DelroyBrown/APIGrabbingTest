# Import the path function from the Django urls module
from django.urls import path

# Import the retrieve_data, detail, and search views from the current directory's views module
from .views import retrieve_data, detail, search

# Define a list of URL patterns for the app
urlpatterns = [
    # Define a URL pattern for the retrieve_data view, accessible at /data/
    # The retrieve_data view will be called when this URL is accessed
    # The name argument is used to refer to this URL pattern in other parts of the code
    path('data/', retrieve_data, name='retrieve_data'),

    # Define a URL pattern for the detail view, accessible at /data/<int:pk>/
    # The detail view will be called when this URL is accessed
    # The <int:pk> part specifies that an integer value will be passed as a parameter named pk to the view
    # The name argument is used to refer to this URL pattern in other parts of the code
    path('data/<int:pk>/', detail, name='detail'),

    # Define a URL pattern for the search view, accessible at /search/
    # The search view will be called when this URL is accessed
    # The name argument is used to refer to this URL pattern in other parts of the code
    path('search/', search, name='search'),

]
