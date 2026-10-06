print("===Trivago-style Travel Package Calculator===")

group_size = int(input("Enter Number of travelers: "))

print("-----Destinations with base price-----")
print("1.Goa    - 20000 ")
print("2.Kerala - 22000 ")
print("3.Manali - 18000 ")
print("4.Jaipur - 15000 ")
des=input("Enter your destination choice (1-4): ")

print("-----Travel Mode-----")
print("1.Flight       - 8000 ")
print("2.Train AC     - 5000 ")
print("3.Train Non-AC - 1500 ")
trav_mode=input("Enter your travel mode choice (1-3): ")

print("-----Hotel Type-----")
print("1.5-Star - 5000 per night")
print("2.3-Star - 3000 per night")
print("3.Budget - 1500 per night")
hotel_type=input("Enter your hotel type choice (1-3): ")
nights=int(input("Enter number of nights: "))

print("-----Meal Plan-----")
print("1.Full Meals     - 4000")
print("2.Breakfast only - 2000")
print("3.No Meals       - 0")
food_plan=input("Enter Food meal plan choice (1-3): ")

print("Sightseeing charges are 3500 per person")
sightseeing=input("Do you want sightseeing? (Y/N): ")

month=input("Enter month of travel (Jan-Dec): ")

print("-----Full Package Details-----")
if des == '1':
    print("Destination: Goa")
    base_price = 20000
elif des == '2':
    print("Destination: Kerala")
    base_price = 22000
elif des == '3':
    print("Destination: Manali")
    base_price = 18000
elif des == '4':
    print("Destination: Jaipur")
    base_price = 15000      
else:
    print("Invalid destination choice. Assuming Goa.")
    des = '1'
    base_price = 20000

if trav_mode == '1':
    print("Travel Mode: Flight") 
    travel_cost = 8000  
elif trav_mode == '2':
    print("Travel Mode: Train AC")
    travel_cost = 5000
elif trav_mode == '3':
    print("Travel Mode: Train Non-AC")
    travel_cost = 1500
else:
    print("Invalid travel mode choice. Assuming Flight.")
    trav_mode = '1'
    travel_cost = 8000

if hotel_type == '1':
    print("Hotel Type: 5-Star")
    hotel_cost = 5000 * nights
elif hotel_type == '2':
    print("Hotel Type: 3-Star")
    hotel_cost = 3000 * nights  
elif hotel_type == '3':
    print("Hotel Type: Budget")
    hotel_cost = 1500 * nights
else:
    print("Invalid hotel type choice. Assuming 5-Star.")
    hotel_type = '1'
    hotel_cost = 5000 * nights

if food_plan == '1':
    print("Food Plan: Full Meals")
    food_cost = 4000
elif food_plan == '2':
    print("Food Plan: Breakfast only")
    food_cost = 2000
elif food_plan == '3':
    print("Food Plan: No Meals")
    food_cost = 0
else:
    print("Invalid food plan choice. Assuming No Meals.")
    food_plan = '3'
    food_cost = 0

if sightseeing == 'Y':
    print("Sightseeing: Included")
    sightseeing_cost = 3500
elif sightseeing == 'N':
    print("Sightseeing: Not Included")
    sightseeing_cost = 0
else:
    print("Invalid input for sightseeing. Assuming No.")
    sightseeing = 'N'
    sightseeing_cost = 0

print("-----Cost Breakdown (Per Person)-----")
print("Base Price: ", base_price)
print("Travel Cost: ", travel_cost)
print("Hotel Cost: ", hotel_cost)
print("Food Cost: ", food_cost)
print("Sightseeing Cost: ", sightseeing_cost)
seasonal_surcharge = 0
if month == 'Jan':
    month = "Jan"
elif month == 'Feb':
    month = "Feb"
elif month == 'Mar':
    month = "Mar"
elif month == 'Apr':
    month = "Apr"
elif month == 'May':
    month = "May"
    seasonal_surcharge = 0.3* (base_price + travel_cost)
elif month == 'Jun':
    month = "Jun"
elif month == 'Jul':
    month = "Jul"
elif month == 'Aug':
    month = "Aug"
elif month == 'Sep':
    month = "Sep"
elif month == 'Oct':
    month = "Oct"
elif month == 'Nov':
    month = "Nov"
elif month == 'Dec':
    month = "Dec"
    seasonal_surcharge = 0.3* (base_price + travel_cost)
else:
    print("Invalid month input. Assuming Jan.")
    month = "Jan"

print("Seasonal Surcharge: ", seasonal_surcharge)

Total_before_discount=base_price+travel_cost+hotel_cost+food_cost+sightseeing_cost+seasonal_surcharge
print("Total Cost before discount: ", Total_before_discount) 

Discount=0
Total=0

if Total_before_discount>=50000:
    Discount=0.1*Total_before_discount
elif Total_before_discount>=40000:
    Discount=0.07*Total_before_discount
print("Discount: ", Discount)

Total_after_discount=Total_before_discount-Discount
GST=0.18*Total_after_discount
print("GST(18%): ", GST)
Total=Total_after_discount+GST
print("Finale Package Price per person: ", Total)

print("===Total Package price for ",group_size," travelers: ", Total*group_size,"===")