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


# In[4]:


# Create a definition for getting the population based on the arguments city_name and year.
def get_pop(city_name, year):
    # Get the inputted city name from the city data dictionary and store it in the city variable.
    city = city_data.get(city_name)
    # If the city name stored in 'city' exists return that city's inputted year otherwise return None.
    if city:
        return city.get(year)
    return None
# Create a main defintion that prompts the user to input a year and city name.
def main():
    # Asks for the user to input a city name and stores it, then checks that the city name exists in the data.
    city_name = input("Enter a city name: ").strip()
    # If the city name does not exist in the data, prompt the user to try again.
    if city_name not in city_data:
        print("City name does not exist in dataset.")
    # Asks the user to input a year in the proper format.
    year = input("Enter a year in the format yrYYYY: ")
    # Create a list of valid year that can be used to check if the inputted year will work.
    valid_years = ["yr1970", "yr1975", "yr1980", "yr1985", "yr1990", "yr1995", "yr2000", "yr2005", "yr2010"]
    # If the year is not part of the valid years list, then prompt the user to try again.
    if year not in valid_years:
        print("Year does not exist, check the format.")
    # Call the get_pop definition based on the inputted city name and year and store it.
    population = get_pop(city_name, year)
    # If the get_pop definiton worked properly and the population variable has float data, print it out.
    if population:
        print(f"The population of {city_name} in {year} was {population} million.")
    # If the data is not in the right format or type by some chance, prompt the user to try again.
    else:
        print("No data available, check the inputs.")
# Call the main definition to start the process for the user.
if __name__ == '__main__':
    main()

