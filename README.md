# CSE20-Assignment-10.1
Description of class:
The class CoffeeMachine is a model of a real life coffee machine.
It uses many different states in order to see if coffee is able to be brewed or not, and if so how long it will take, and what kind of coffee it will brew.
Description of variables:
coffee_amount: the amount of coffee to be brewed. affects the amount of time to brew, and how watery the coffee is (g,int)
water_amount: the amount of water put into the machine, affects how watery the coffee is (ml,int)
power: boolean, either power is on or off (needs to be on for machine to run)
filter: boolean, either filter is clean or not (needs to be clean to run)
coffee_type: the type of coffee that will brew, has no effect on the brewing except for the end statement.
coffee_added: boolean, either coffee is added or not. (coffee needs to be added to run the machine)
water_added: boolean, either water is added or not. (water needs to be added to run)
time_to_brew: (float)the amount of time in seconds it takes to brew the coffee. calculated by dividing the amount of coffee by 5
ratio: (float)the ratio of coffee to water, determines how strong/watery the coffee is
ideal_ratio: the ratio of coffee/water that leads to perfect coffee
upper_ender: the ratio of coffee/water that leads to slightly stronger coffee
lower_end: the ratio of coffee/water that leads to slightly watery coffee
cups_of_coffee: the amount of cups that are brewed (to be displayed in the final returned statement)
Description of methods:
__init__: requires coffee_added, water_added, coffee_type, coffee_amount, water_amount,power,filter)
doesn't return anything
set_coffee_type: requires new_coffee_type
doesn't return anything, just chnages the coffee type variable
get_coffee_type: doesn't require an arg
returns coffee_type
add_coffee: requires coffee_amount
changes the coffee_amount variable to the input, and returns a statement saying how much was added
get_coffee_status: requires no args
returns the coffee_added boolean
add_water: requires water_amount
sets water_added to true, and sets the water amount to the new arg, returns a statement saying how much was added
get_water_status: requires no args
returns the water_added boolean
turn_power_on: requires no args
returns nothing, changes the power var to True
change_filter: requires no args
sets filter to True
get_filter_status: requires no args
returns the filter boolean
brew_coffee: requires no args
calculates whether coffee can be brewed or not, and if it can, what kind will be brewed. then returns a statement saying what was brewed
menu: requires no args
interface for the user to interact with the program through. returns print statements saying what actions have been done

Instructions:
The demo program just runs the menu function, and says to brew the best cup of coffee possible.
A user can run my program by downloading it, and running it. No extra files neccessary.
If the main function isn't there, the user just needs to type
    coffee1 = CoffeeMachine()
    coffee1.menu()
