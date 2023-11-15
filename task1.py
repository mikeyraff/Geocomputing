#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import csv module to have access to DictReader function.
import csv
# Create a definition for reading in the csv file that takes one argument, the csv file.
def read_csv(filename):
    # Create a dictionary that will get keys and values added to it from the csv file.
    data = {}
    # Open the filename and reads in the data using 'r' and stores it in file variable.
    with open(filename, 'r') as file:
        # csv.DictReader returns a class instance and makes the data easy to loop over. 
        reader = csv.DictReader(file)
        # Loops through class instance with the csv data.
        for row in reader:
            # Creates key variable for the data dictionary that is the city name, which is under the 'label column' in the csv file.
            city_name = row['label']
            # The corresponding value is another dictionary that represents the data for that particular city.
            data[city_name] = row
    return data
# Run the function on the csv file of interest and store it in a variable
city_data = read_csv('CityPop.csv')
# Print the data to see that the dictionary properly has the city key and values of the city's data from the csv file.
print(city_data)

