class Rental_Income:
    """Initialize Attributes for class Rental_Income"""
    def __init__(self, expTax, expIns, expUtil, expHoa, expLawn, expVacant, expRepairs, expCapex, expPropMgt, expMortgage, propInc, propExp, unitInc):
        # self.propId = propId
        # self.numUnits = numUnits
        # self.estRentIncome = estRentIncome
        # self.unitId = unitId
        # self.otherIncome = otherIncome
        self.expTax = expTax
        self.expIns = expIns
        self.expUtil = expUtil
        self.expHoa = expHoa
        self.expLawn = expLawn
        self.expVacant = expVacant
        self.expRepairs = expRepairs
        self.expCapex = expCapex
        self.expPropMgt = expPropMgt
        self.expMortgage = expMortgage
        self.propInc = {}
        self.propExp = {}
        self.unitInc = {}



    def monthlyInc(self):
        """
            monthlyInc method/function
            Takes user input to calculate total estimated monthly income
            expected from rental property
        """
        # Not sure yet if I want to include this one
        # num_reviewing = input("How many properties are you reviewing?")
        # or after finishing one property, ask would you like to calculate ROI for another property? y/n/exit program
   

        # Property name/address to identify which prop reviewed
        prop_id = input("What is the property name or address number? ")
        
        # Set value for prop_id in propInc dict to 0 in order to += with rental income values later
        self.propInc[prop_id] = 0
        print(self.propInc)


        # Get user input to determine number of units in property (must be a number)
        while True:
            try:
                num_units = int(input("How many units are in the property? Please enter a number value. "))
                break
            except ValueError:
                print("The input must be a number.")
        

        # If property has 1 unit, ask monthly est_rent_ income for the property
        if num_units == 1:
            est_rent_income = int(input(f"What is the estimated monthly rental income for the property? Please enter a number value. "))

        # If prop has more than 1 unit, ask monthly est_rent_income for each unit
        if num_units > 1:

            # Variable stores the num of units provided by user as a range from 1 to the number provided by user
            num_units = list(range(1,num_units+1))

            # Ask user to identify the unit and its monthly rental income
            for unit in num_units:
                unit_id = input("Enter the unit name or number. ")

                est_rent_income = int(input(f"What is the monthly rental income for unit {unit_id.title()}? Please enter a number value. "))

                # Not sure yet if I need the unitInc dictionary
                self.unitInc[unit_id] = est_rent_income
                
                # Add the est_rent_income for each unit to the existing value in the propInc dict (summing ongoing to get a total est income)
                self.propInc[prop_id] += est_rent_income

                # Store unit_id to unitInc dict key and est_rent_income to unitInc dict value
                print(self.unitInc)
                print(self.propInc)

        # Ask about possible additional income
        addl_inc = input("Do you expect additional income from this property (such as laundry, storage, or other miscellaneous income)? Yes or No: ")
        
        # Add additional income amount to value in propInc dict.
        if addl_inc.lower() == 'yes':
            other_inc = int(input("Please enter the estimated amount of additional monthly income expected. "))
          
            self.propInc[prop_id] += other_inc   
            print(self.propInc)



def monthlyExp(self):







calcRoi = Rental_Income(1,1,1,1,1,1,1,1,1,1,1,1,1)

def run():
    while True:
    
        get_started = input("Would you like to evaluate the ROI on a rental property? Type Yes to get started or No to exit. ")

        if get_started.lower() == 'no':
            print("You have exited the program")
            break

        elif get_started.lower() == 'yes':
            calcRoi.monthlyInc()

run()




   
    


