#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# Created a defintion that calculates the population change based on the start and end year inputted by the user.
def calculate_population_change(city, start_year, end_year):
# Gets the populations from city_data of the cities for the year inputted and converts them to floats.
    try:
        start_population = float(city[start_year])
        end_population = float(city[end_year])
# Subtracts the population values for end and start year to get the change and returns it, returns None if ValueError occurs.
        return end_population - start_population
    except ValueError:
        return None
# Created a main definition that gets the years of interest from the user.
def main():
    # Created a list of valid years that will be used to check the inputted years are valid.
    valid_years = ["yr1970", "yr1975", "yr1980", "yr1985", "yr1990", "yr1995", "yr2000", "yr2005", "yr2010"]
    # Get years from the user and strips them to make sure no whitespace that can cause errors.
    start_year = input(f"Enter the start year in format 'yrYYYY': ").strip()
    end_year = input(f"Enter the end year in format 'yrYYYY': ").strip()
    # Check if the entered years are valid options and in the right format, if not returns an error statement.
    if start_year not in valid_years or end_year not in valid_years:
        print("Invalid year format. Please enter in 'yrYYYY' format and try again.")
        return
    # Calculate population change for all cities and store results in a list.
    results = []
    # Loops through the values in the city_data and appends the population change variable to the data.
    for city in city_data.values():
        change = calculate_population_change(city, start_year, end_year)
        if change is not None:
    # Alters the results so only the id, city and population change are portrayed in the new csv file.
            results.append({
                "id": city["id"],
                "city": city["label"],
                "population_change": change
            })

    # Write the results to a new csv file with a new name and specified field names
    with open("CityPopChg.csv", "w", newline="") as file:
        fieldnames = ["id", "city", "population_change"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Writes the new csv and store it in the proper repository and prints a message when successful.
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    print("Population change data has been written to CityPopChg.csv.")
# Prompts the user to input the two years when cell is ran.
if __name__ == '__main__':
    main()


# We have the calculate_population_change function which calculates the population change for a specific city between the two years provided.
# The main function prompts the user for the start and end years, validates the input, calculates the population change for all cities, and then writes the results to CityPopChg.csv.
