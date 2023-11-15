#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[4]:


# Import the math module to convert the latitude and longitude to radians and use trig in the distance equation.
import math

# Created a definition that takes in the 4 coordinate inputs and converts them to radian values, which can be used for the equation.
def greater_distance(lat1, lon1, lat2, lon2):    
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
# Using the math module and inputs, the angle is calcualted and later multiplied by the radius of the Earth to get spherical distance.
    angle = math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)))
    R = 6300
    d = angle * R
    return d
# Created a main definition where the user will input the cities and the distance is calculated and printed.
def main():
# Get city names from the user and uses strip() to get ride of any whitespace in the city name.
    city_name1 = input("Enter the name of the first city: ").strip()
    city_name2 = input("Enter the name of the second city: ").strip()
# Check if the entered cities exist in the city_data variable from task 1.
    if city_name1 not in city_data or city_name2 not in city_data:
# If the city names are not in the data set, the user will be prompted with an error message.
        print("One or both city names are invalid. Please check the names and try again.")
        return
# Extract latitudes and longitudes for both cities and makes sure the values are in the type float.
    lat1, lon1 = float(city_data[city_name1]['latitude']), float(city_data[city_name1]['longitude'])
    lat2, lon2 = float(city_data[city_name2]['latitude']), float(city_data[city_name2]['longitude'])
    # Calculate the distance using the greater distance formula in the previous definition
    distance = greater_distance(lat1, lon1, lat2, lon2)
    # Prints the distance between the two inputted cities in a clear sentence.
    print(f"The distance between {city_name1} and {city_name2} is {distance:.2f} km.")
# Prompts the main definition once the cell is ran.
if __name__ == '__main__':
    main()


# We have the haversine_distance function which calculates the great-circle distance between two points given their latitudes and longitudes.
# The main function prompts the user for two city names, validates them, extracts their latitude and longitude values, and calculates the distance between them.
# The result is then displayed to the user.
