class Roi_Calc:
    """Initialize Attributes for class Roi_Calc"""
    def __init__(self, propId, estRentIncome, expenseTax, expenseInsurance, expenseUtilities, expenseHoa, expenseLawnCare, expenseVacancy, expenseRepairs, expenseCapExpenditures, expensePropertyMgmt, expenseMortgage, downPayment, closingCosts, rehabBudget, otherMiscCosts, purchasePrice, calcMonthlyCashFlow, calcAnnualCashFlow, annualCashFlow, propInc, propExp, unitInc, upFrontInvestment, calcRoi, percentageRoi):
        self.propId = propId
        self.estRentIncome = estRentIncome
        self.expenseTax = expenseTax
        self.expenseInsurance = expenseInsurance
        self.expenseUtilities = expenseUtilities
        self.expenseHoa = expenseHoa
        self.expenseLawnCare = expenseLawnCare
        self.expenseVacancy = expenseVacancy
        self.expenseRepairs = expenseRepairs
        self.expenseCapExpenditures = expenseCapExpenditures
        self.expensePropertyMgmt = expensePropertyMgmt
        self.expenseMortgage = expenseMortgage
        self.downPayment = downPayment
        self.closingCosts = closingCosts
        self.rehabBudget = rehabBudget
        self.otherMiscCosts = otherMiscCosts
        self.purchasePrice = purchasePrice
        self.calcMonthlyCashFlow = {}
        self.calcAnnualCashFlow = calcAnnualCashFlow
        self.annualCashFlow = {}
        self.propInc = {}
        self.propExp = {}
        self.unitInc = {}
        self.upFrontInvestment = {}
        self.calcRoi = calcRoi
        self.percentage_Roi = percentageRoi



    def calculateMonthlyInc(self):
        """
            monthlyInc method/function
            Takes user input to calculate total estimated monthly income
            expected from rental property
        """
        # Not sure yet if I want to include this one
        # num_reviewing = input("How many properties are you reviewing?")
        # or after finishing one property, ask would you like to calculate ROI for another property? y/n/exit program

        print("\nWe will start by calculating the estimated income you expect to receive from the rental property.\n")

        # Property name/address to identify which prop reviewed
        property_id = input("\nWhat is the property name or address number? ")
        self.propId = property_id
        

        # Set value for prop_id in propInc dict to 0 in order to += with rental income values later
        self.propInc[self.propId] = 0
        
        # ER use to print for confirmation
        # print(self.propInc)


        # Get user input to determine number of units in property (must be a number)
        while True:
            try:
                num_units = int(input("\nHow many units are in the property? Please enter a number value: "))
                break
            except ValueError:
                print("The input must be a number.")


        # If property has 1 unit, ask monthly est_rent_ income for the property
        if num_units == 1:
            est_rent_income = int(input(f"\nWhat is the estimated monthly rental income for the property? Please enter a number value: "))

            # increment the dictionary value by est_rent_income            
            self.propInc[self.propId] += est_rent_income
            
            # ER use to print for confirmation
            # print(self.propInc)


        # If prop has more than 1 unit, ask monthly est_rent_income for each unit
        if num_units > 1:

            # Variable stores the num of units provided by user as a range from 1 to the number provided by user
            num_units = list(range(1,num_units+1))

            # Ask user to identify the unit and its monthly rental income
            for unit in num_units:

                # If allowing user to identify individual units, need to prevent appending dups to dictionary
                # unit_id = input("\nEnter the unit name or number: ")

                # For each unit in num_units, ask monthly rental income
                est_rent_income = int(input(f"\nWhat is the monthly rental income for unit {unit}? Please enter a number value: "))

                # Add keys, values for each unit to unitInc dictionary
                self.unitInc[unit] = est_rent_income
                
                # Add the est_rent_income for each unit to the existing value in the propInc dict (summing ongoing to get a total est income)
                self.propInc[self.propId] += est_rent_income

                # ER use to print for confirmation
                # print(self.unitInc)
                # print(self.propInc)


        # Ask about possible additional income for the property
        additional_income = input("\nDo you expect additional income from the property (such as laundry, storage, or other miscellaneous income)? Yes or No: ")
        
        # Add additional income amount to value in propInc dict.
        if additional_income.lower() == 'yes':
            est_additional_income = int(input("\nPlease enter the estimated amount of additional monthly income expected: "))
          
            self.propInc[self.propId] += est_additional_income

        
        # any value other yes, increment by 0. Incrementing not working properly without this step. 
        else: 
            self.propInc[self.propId] += 0
        
        
        # Display a summary of total estimated income
        print(f"\nBased on your inputs, the total estimated income for property '{self.propId.title()}' is: $",format(self.propInc[self.propId],",.2f"))


    def calculateMonthlyExp(self):
        """
            monthlyExp method/function will obtain user input to calculate monthly expenses associated with rental property
        """

        print("\nNext, we will calculate estimated expenses associated with the rental property.\n")

        # Set value for prop_id in propInc dict to 0 in order to += with rental income values later
        self.propExp[self.propId] = 0
        # print(f"Property Expenses Dictionary: {self.propExp}\n")


        # Ask user a series of inputs to gather expense amounts
        # Increment each response to values in self.propExp dictionary based on self.propId key
        tax_budget = int(input("\nPlease enter the estimated monthly taxes for the property. Enter 0 if not applicable or don't know: "))
        self.expenseTax = tax_budget
        self.propExp[self.propId] += self.expenseTax


        utilities_budget = int(input("\nPlease enter the estimated monthly utility costs for the property. Enter 0 if not applicable or don't know: "))
        self.expenseUtilities = utilities_budget
        self.propExp[self.propId] += self.expenseUtilities


        insurance_budget = int(input("\nPlease enter the estimated monthly insurance costs for the property. Enter 0 if not applicable or don't know: "))
        self.expenseInsurance = insurance_budget
        self.propExp[self.propId] += self.expenseInsurance


        hoa_budget = int(input("\nPlease enter the estimated monthly HOA fees for the property. Enter 0 if not applicable or don't know: "))
        self.expenseHoa = hoa_budget
        self.propExp[self.propId] += self.expenseHoa


        lawn_care_budget = int(input("\nPlease enter the estimated monthly budget for lawn care/snow removal for the property. Enter 0 if not applicable or don't know: "))
        self.expenseLawnCare = lawn_care_budget
        self.propExp[self.propId] += self.expenseLawnCare


        vacancy_budget = int(input("\nPlease enter your estimated monthly budget for vacancies. Enter 0 if not applicable or don't know: "))
        self.expenseVacancy = vacancy_budget
        self.propExp[self.propId] += self.expenseVacancy

    
        repairs_budget = int(input("\nPlease enter your estimated monthly budget for repairs (i.e. small damages to property, such as holes in a wall, minor flooring repairs, paint touch-up, etc.). Enter 0 if not applicable or don't know: "))
        self.expenseRepairs = repairs_budget
        self.propExp[self.propId] += self.expenseRepairs


        cap_expenditure_budget = int(input("\nPlease enter your estimated monthly budget for capital expenditures (i.e. high-cost items, such as a new roof, new appliances, new flooring, etc.). Enter 0 if not applicable or don't know: "))
        self.expenseCapExpenditures = cap_expenditure_budget
        self.propExp[self.propId] += self.expenseCapExpenditures
        

        property_mgmt_budget = int(input("\nPlease enter your estimated monthly cost for property management. Enter 0 if not applicable or don't know: "))
        self.expensePropertyMgmt = property_mgmt_budget
        self.propExp[self.propId] += self.expensePropertyMgmt
        

        mortgage_budget = int(input("\nPlease enter your estimated monthly mortgage amount. Enter 0 if not applicable or don't know: "))
        self.expenseMortgage = mortgage_budget
        self.propExp[self.propId] += self.expenseMortgage

        
        # Print a summary of expenses
        # print(f"Property Expenses Dictionary: {self.propExp}")

        # Display a summary of total estimated expenses
        print(f"\nBased on your inputs, the total estimated expense amount for property '{self.propId.title()}' is: $",format(self.propExp[self.propId],",.2f"))

    
    def calculateCashFlow(self):
        """
            calcCashFlow function/method
            will calculate cash flow using values from
            propInc and propExp dictionaries
        """

        # Set the self.calcMonthlyCashFlow empty dictionary to store the value of the monthly cash flow calculation
        self.calcMonthlyCashFlow = {x: self.propInc[x] - self.propExp[x] for x in self.propInc if x in self.propExp}


        # Set annualCashFlow dictionary value to self.propId and its value to 0 in order to increment based on user inputs
        self.annualCashFlow[self.propId] = 0
        # print(f"Annual Cash Flow Dictionary: {self.annualCashFlow}\n")
    
        # Loop through each property in the self.propInc dictionary
        for prop in self.propInc: 
            
            # Calculate annual cash flow based on self.calcMonthlyCashFlow *12
            # Add value to self.annual CashFlow dictionary
            self.calcAnnualCashFlow = self.calcMonthlyCashFlow[self.propId]*12
            self.annualCashFlow[self.propId] += self.calcAnnualCashFlow

            
            # Display monthy and annual cash flow amounts
            print(f"\nWe calculate Cash Flow as projected income less projected expenses. Based on the information you provided, your estimated monthly cash flow for property '{self.propId.title()}' is: $",format(self.calcMonthlyCashFlow[self.propId],",.2f"))


            print(f"\nThe projected annual cash flow is: $",format(self.annualCashFlow[self.propId],",.2f"))

            # ER use to print for confirmation
            # print(self.calcMonthlyCashFlow.items())
            # print(self.annualCashFlow.items())



    def calculateInitialInvestment(self):
        print("\nFinally, we are going to calculate your initial investment (the amount you are putting in up-front for the purchase of the rental property).")

        # Set upFrontInvestment dictionary value to 0 in order to increment based on user inputs
        self.upFrontInvestment[self.propId] = 0

        # Ask user series of inputs to determine up-front investment amount
        purchase_price = int(input("\nWhat is the purchase price of the property? Enter a numerical value: "))
        # self.purchasePrice = purchase_price
        # self.upFrontInvestment[self.propId] += self.purchasePrice


        closing_costs = int(input("\nPlease enter your estimated closing costs. Enter 0 if not applicable or don't know. Or enter an estimated amount of 3-5% of the purchase price: "))
        self.closingCosts = closing_costs
        self.upFrontInvestment[self.propId] += self.closingCosts


        down_payment = int(input("\nPlease enter your down payment amount. Enter 0 if not applicable or don't know: "))
        self.downPayment = down_payment
        self.upFrontInvestment[self.propId] += self.downPayment


        rehab_budget = int(input("\nPlease enter your rehab budget (i.e. painting the outside of the property, other cosmetic changes, or bigger changes such as fixing electrical/plumbing/roofing issues). Enter 0 if not applicable or don't know: "))
        self.rehabBudget = rehab_budget
        self.upFrontInvestment[self.propId] += self.rehabBudget


        other_misc_costs = int(input("\nPlease enter the total amount of any other up-front investment costs you anticipate. Enter 0 if not applicable or don't know: "))
        self.otherMiscCosts = other_misc_costs
        self.upFrontInvestment[self.propId] += self.otherMiscCosts


        print(f"\nBased on your input, the total up-front investment cost is: $",format(self.upFrontInvestment[self.propId],".2f"))


    def calculateRoi(self):
        """
            calculateRoi method/function
            calculates annual ROI by:
            annual cash flow divided by total investment
        """

        # Caculation for annual ROI. Annual cash flow/total investment
        self.calcRoi = (self.annualCashFlow[self.propId] / self.upFrontInvestment[self.propId])

        # Change self.calcRoi from decimal display to percentage
        self.percentageRoi = "{:.2%}".format(self.calcRoi)

        # Display ROI result and opinion based on greater than 8% == good
        if self.calcRoi < .08:
         
            print(f"\nWe calculate Return on Investment (ROI) as the projected annual cash flow divided by total investment. Based on the information you provided, your estimated annual ROI for property '{self.propId.title()}' is: {self.percentageRoi}")

            print(f"\nWe consider anything over 8% to be a good return on investment. Based on your inputs, we consider property '{self.propId.title()}' a poor return on investment.\n")

        else:
    
            print(f"\nWe calculate Return on Investment (ROI) as the projected annual cash flow divided by total investment. Based on the information you provided, your estimated annual ROI for property '{self.propId.title()}' is: {self.percentageRoi}")

            print(f"\nWe consider anything over 8% to be a good return on investment. Based on your inputs, we consider property '{self.propId.title()}' a good return on investment!\n")




rentalProp = Roi_Calc(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

def run():
    while True:
    
        get_started = input("Would you like to evaluate the ROI on a rental property? Type Yes to get started or No to exit. ")

        if get_started.lower() == 'no':
            print("You have exited the program.")
            break

        elif get_started.lower() == 'yes':
            rentalProp.calculateMonthlyInc()
            rentalProp.calculateMonthlyExp()
            rentalProp.calculateInitialInvestment()
            rentalProp.calculateCashFlow()
            rentalProp.calculateRoi()
            print("Thank you for using our ROI rental property calculator!")
            break

run()




   
    


