# user input holiday details, cast string to integer for num_nights and rental_days
city_flight = input("Which city are you flying to? (London/Glasgow/Birmingham/Cardiff) ")
city_flight = city_flight.upper() #convert to uppercase to avoid error if user inputs upper/lower case 
num_nights = int(input("How many nights will you be staying? "))
rental_days = int(input("How many days will you require a car rental? "))

# function to calculate hotel cost with num_nights as the parameter 
# when num_nights is passed into the function, returns num_nights x 70 
def hotel_cost(num_nights):
    hotel = int(num_nights * 70)
    return hotel

# function to calculate flight cost, with city_flight as the parameter
# return flight cost depending on which city is inputed 
def plane_cost(city_flight):
    if city_flight == "LONDON":
        flight = 100
    elif city_flight == "GLASGOW":
        flight = 120
    elif city_flight == "BIRMINGHAM":
        flight = 80
    elif city_flight == "CARDIFF":
        flight = 85
    return flight

# function to calculate cost of car rental with rental_days as parameter 
# returns rental_days x 50 
def car_rental(rental_days):
    rental = rental_days * 50
    return rental 

# Sum of 3 functions with the relevant parameters to calculate total cost
holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
print(f"\nThe total cost of your holiday will be: £{holiday_cost}")
print(f"Destination: {city_flight}\nCost of flight: £{plane_cost(city_flight)}\nLength of Stay: {num_nights}\nCost of Hotel: £{hotel_cost(num_nights)}")
print(f"Number of days for car rental: {rental_days}\nCost of car rental: £{car_rental(rental_days)}")
