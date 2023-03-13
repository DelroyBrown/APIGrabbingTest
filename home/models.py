from django.db import models

# Define the ChallengeAPI model
class ChallengeAPI(models.Model):
    # Create an auto-incrementing primary key field
    id = models.AutoField(primary_key=True)
    
    # Create a char field to store the name with a max length of 100 characters
    name = models.CharField(max_length=100)
    
    # Create a decimal field to store the price with a max of 5 digits and 2 decimal places
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Create a positive integer field to store the quantity
    quantity = models.PositiveIntegerField()
    
    # Define metadata for the model
    class Meta:
        # Specify the table name in the database
        db_table = 'home_product'
    
    # Define a string representation of the model instance
    def __str__(self):
        # Return the name of the model instance
        return self.name
