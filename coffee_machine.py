# Luca Menotti
# 11/29/2021
# CSE20 Assignment 10.1

# importing time module to use sleep() later
import time

# class CoffeeMachine: simulates a coffee machine, where you can brew coffee. 
# Takes into account the type of coffee, the amount, the amount of water, if there is power on, and if there is a clean filter
# All conditions for the machine to work have to be met, or else the machine will not brew coffee. 
class CoffeeMachine:
    # init function that sets the default state of everything and creates variables that will be referenced later
    def __init__(self, coffee_added=False,water_added=False,coffee_type="Arabica",coffee_amount=0,water_amount=0, power=False, filter=False):
        self.__coffee_amount = coffee_amount
        self.__water_amount = water_amount
        self.__power = power
        self.__filter = filter
        self.__coffee_type = coffee_type
        self.__coffee_added = coffee_added
        self.__water_added = water_added
    
    # set_coffee_type: takes in the new coffee type that the user wishes to brew as a string, and replaces the old one with it
    def set_coffee_type(self,new_coffee_type):
        self.__coffee_type = str(new_coffee_type)
    # get_coffee_type: just gets the current coffee type and returns it
    def get_coffee_type(self):
        return(self.__coffee_type)

    # add_coffee: takes in the amount of coffee to add, and adds it to the amount variable
    def add_coffee(self,coffee_amount):
        self.__coffee_amount = coffee_amount
        # sets the coffee added variable to true, which gives the brew coffee function a green light
        self.__coffee_added = True
        # then returns the amount added and the type added
        return(f"You have added {coffee_amount}g of {self.__coffee_type} bean coffee")
    # returns whether coffee has been added or not
    def get_coffee_status(self):
        if self.__coffee_added==True:
            print(f"{self.__coffee_amount}g of {self.__coffee_type} coffee have been added")
            return(True)
        if self.__coffee_added == False:
            print("No coffee has been added yet")
            return(True)        
    
    # takes in an amount int or float and sets the water amount to it
    def add_water(self,water_amount):
        self.__water_amount = water_amount
        # sets water added boolean to true to give the green light
        self.__water_added = True
        return(f"You have added {water_amount} ml of water")
    # same thing as the get coffee status function, but for water
    def get_water_status(self):
        if self.__water_added==True:
            print(f"{self.__water_amount}ml of water have been added")
            return(True)
        if self.__water_added == False:
            print("No water has been added yet")
            return(False)

    # sets the power boolean to true (from a default of false)
    def turn_power_on(self):
        self.__power = True

    # sets the filter boolean to true (from a default of false)
    def change_filter(self):
        self.__filter = True
        # returns a message saying there is a new filter
        #return("There is now a new filter")
    # returns whether the filter status is false or true
    def get_filter_status(self):
        if self.__filter==True:
            print("There is a working filter in place")
            return(True)
        if self.__filter == False:
            print("There is no working filter in place")
            return(False)

    # brew_coffee: the central function of the coffee machine which brews the coffee
    def brew_coffee(self):
        # checks all the other variables of the machine to make sure the machine is set to go
        if self.__filter == False:
            return("You can't brew coffee with a used filter! Please change the filter.")
        elif self.__power == False:
            return("You can't brew coffee without turning the coffee machine on! Please turn the coffee machine on.")
        elif self.__water_added == False:
            return("You can't brew coffee without adding water first! Please add water.")
        elif self.__coffee_added == False:
            return("You can't brew coffee without adding the coffee first! Please add coffee.")
        # if all variables are in order, starts the machine    
        else:
            # calculating the amount of time to brew, which in this machine is 4 seconds for a cup of coffee
            time_to_brew = self.__coffee_amount/5 
            # calculates the ratio of coffee to water in the machine, which will result in different strengths of coffee
            ratio = self.__coffee_amount/self.__water_amount
            # the ideal ratio is based on 20g of coffee to 300ml of water
            ideal_ratio = 1/15
            # this represents coffee that has slighty more coffee and therefore stronger
            upper_end = 1/15*1.2
            # this represents coffee that has slightly less coffee and therefore weaker
            lower_end = 1/15*0.8
            # calculates the amount of cups that are produced
            self.__cups_of_coffee = self.__coffee_amount/20
            #simple if/else just to ensure that a decimal amount of cups of coffee isnt rounded down to 0 or up to 1 when converting to int
            # if the amount is above one, it looks much clear to round with an int
            if self.__cups_of_coffee > 1:
                self.__cups_of_coffee = int(self.__cups_of_coffee)
            else:
                self.__cups_of_coffee = float(self.__cups_of_coffee)
            # prints a statement saying how long it will take to brew
            print(f"Brewing coffee! This will take {time_to_brew} seconds.")
        # sets the filter, water, and coffee to false (as they will all be used up after brewing a cup of coffee)
        self.__filter = False
        self.__water_added = False
        self.__coffee_added = False
        # time.sleep function that just pauses everything until the amount of time is up. this will be how long it takes to brew the coffee
        #time.sleep(time_to_brew)
        while True:
            if time_to_brew > 0:
                time.sleep(1)
                time_to_brew = time_to_brew -1 
                print(".")
            if time_to_brew <= 0:
                break
        # lots of if statements that show the end result. if the coffee is within the safe range it will be either slightly strong coffee, slightly weak coffee, or perfect coffee
        # if it is out of the bounds, it will be way too strong or super watery
        # returns the end result of amount of cups brewed of what type, and how strong it is
        if ratio > ideal_ratio and ratio < upper_end:
            return(f"You have successfully brewed {self.__cups_of_coffee} cup(s) of slightly stronger than usual {self.__coffee_type} coffee! Enjoy.")
        elif ratio < ideal_ratio and ratio > lower_end:
            return(f"You have successfully brewed {self.__cups_of_coffee} cup(s) of slightly weaker than usual {self.__coffee_type} coffee! Enjoy.")      
        elif ratio > upper_end:
            return(f"You have successfully brewed {self.__cups_of_coffee} cup(s) of way too strong {self.__coffee_type} coffee! Good luck drinking it.")       
        elif ratio < lower_end:
            return(f"You have successfully brewed {self.__cups_of_coffee} cup(s) of super watery {self.__coffee_type} coffee! Is this even worth drinking?")  
        elif ratio == ideal_ratio:
            return(f"Wow! You have successfully brewed {self.__cups_of_coffee} perfect cup(s) of {self.__coffee_type} coffee! I am impressed.")

    # menu function, which allows the user to interface with the program and execute all functions without having to go into the code
    def menu(self):
        print("Welcome to the coffee machine!")
        # for loop that continuously prompts the user until exited
        while True:
            # slight delay between prompts to make it less jarring
            time.sleep(0.1)
            (x) = input("Please type an action. Actions: add coffee, change coffee type, get coffee status, add water, get water status, turn on power, change filter,get filter status, brew coffee, exit\n")
            x = x.capitalize()
            # if add coffee is chosen, it executes the add coffee function
            if x == "Add coffee":
                # while loop that just ensures that the input is a valid number, if it isn't it prompts the user again
                while True:
                    z = input("How much coffee (in grams) would you like to add?\n")
                    try: 
                        z = float(z)
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                        pass
                CoffeeMachine.add_coffee(self,z)
                print(f"{CoffeeMachine.add_coffee(self,z)}")
            # if change coffee type is chosen, it asks the user for input and then uses the input in the set coffee type function
            elif x == "Change coffee type":
                    z = input("What would you like to change the coffee type to?\n")
                    CoffeeMachine.set_coffee_type(self,z)
                    print(f"Coffee type has been changed")
            # if get coffee status chosen, simply prints out the get coffee status function
            elif x == "Get coffee status":
                print(CoffeeMachine.get_coffee_status(self))
            # if add water is chosen, prompts the user for input and then executes it in the add water function
            elif x == "Add water":
                # wihle loop to ensure proper input
                while True:
                    z = input("How much water (in ml) would you like to add?\n")
                    try: 
                        z = float(z)
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                        pass
                CoffeeMachine.add_water(self,z)
                print(CoffeeMachine.add_water(self,z))  
            # if water status is chosen, just does the get water status function  
            elif x == "Get water status":
                print(CoffeeMachine.get_water_status(self))   
            # if turn on power is chosen, uses the turn on power function
            elif x == "Turn on power":
                CoffeeMachine.turn_power_on(self)
                print("Power has been turned on")
            # if change filter is chosen, uses the turn on filter function
            elif x == "Change filter":
                CoffeeMachine.change_filter(self)
                print("Filter has been changed")
            # if get filter status chosen, uses the get filter status function
            elif x=="Get filter status":
                print(CoffeeMachine.get_filter_status(self))
            # if brew coffee is chosen, it uses the filter status function
            elif x == "Brew coffee":
                print(CoffeeMachine.brew_coffee(self))   
            # if exit is chosen, closes the menu and program
            elif x=="Exit":
                return(print("Exiting coffee machine menu"))
            # in case a proper action isn't chosen, prompts the user again
            else:
                print("Please enter a valid action")
            

# main function
def main():
    print("Brew the best cup of coffee possible!")
    coffee1 = CoffeeMachine()
    coffee1.menu()

# calling the main function
if __name__ == "__main__":
    main()