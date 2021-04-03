class Roi_Calc:
    """Initialize Attributes for class Roi_Calc"""
    def __init__(self, propId, estRentIncome, expenseTax, expenseInsurance, expenseUtilities, expenseHoa, expenseLawnCare, expenseVacancy, expenseRepairs, expenseCapExpenditures, expensePropertyMgmt, expenseMortgage, downPayment, closingCosts, rehabBudget, otherMiscCosts, purchasePrice, propInc, propExp, unitInc, upFrontInvestment):
        self.propId = propId
        self.estRentIncome = estRentIncome
        # self.numUnits = numUnits
        # self.unitId = unitId
        # self.otherIncome = otherIncome
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
        self.propInc = {}
        self.propExp = {}
        self.unitInc = {}
        self.upFrontInvestment = {}



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
        property_id = input("What is the property name or address number? ")
        self.propId = property_id
        

        # Set value for prop_id in propInc dict to 0 in order to += with rental income values later
        self.propInc[self.propId] = 0
        print(self.propInc)


        # Get user input to determine number of units in property (must be a number)
        while True:
            try:
                num_units = int(input("How many units are in the property? Please enter a number value: "))
                break
            except ValueError:
                print("The input must be a number.")


        # If property has 1 unit, ask monthly est_rent_ income for the property
        if num_units == 1:
            est_rent_income = int(input(f"What is the estimated monthly rental income for the property? Please enter a number value: "))

            # increment the dictionary value by est_rent_income            
            self.propInc[self.propId] += est_rent_income
            print(self.propInc)


        # If prop has more than 1 unit, ask monthly est_rent_income for each unit
        if num_units > 1:

            # Variable stores the num of units provided by user as a range from 1 to the number provided by user
            num_units = list(range(1,num_units+1))

            # Ask user to identify the unit and its monthly rental income
            for unit in num_units:
                unit_id = input("Enter the unit name or number: ")

                est_rent_income = int(input(f"What is the monthly rental income for unit {unit_id.title()}? Please enter a number value: "))

                # Not sure yet if I need the unitInc dictionary
                self.unitInc[unit_id] = est_rent_income
                
                # Add the est_rent_income for each unit to the existing value in the propInc dict (summing ongoing to get a total est income)
                self.propInc[self.propId] += est_rent_income

                # Store unit_id to unitInc dict key and est_rent_income to unitInc dict value
                print(self.unitInc)
                print(self.propInc)


        # Ask about possible additional income for the property
        additional_income = input("Do you expect additional income from the property (such as laundry, storage, or other miscellaneous income)? Yes or No: ")
        
        # Add additional income amount to value in propInc dict.
        if additional_income.lower() == 'yes':
            est_additional_income = int(input("Please enter the estimated amount of additional monthly income expected: "))
          
            self.propInc[self.propId] += est_additional_income
            print(self.propInc)
        
        # any value other yes, increment by 0. Incrementing not working properly without this step. 
        else: 
            self.propInc[self.propId] += 0
            print(self.propInc)



    def calculateMonthlyExp(self):
        """
            monthlyExp method/function will obtain user input to calculate monthly expenses associated with rental property
        """

        print("Next, we will calculate estimated expenses associated with the rental property.\n")

        # Set value for prop_id in propInc dict to 0 in order to += with rental income values later
        self.propExp[self.propId] = 0
        print(f"Property Expenses Dictionary: {self.propExp}")


        tax_budget = int(input("Please enter the estimated monthly taxes for the property. Enter 0 if not applicable or don't know: "))
        self.expenseTax = tax_budget
        self.propExp[self.propId] += self.expenseTax


        utilities_budget = int(input("Please enter the estimated monthly utility costs for the property. Enter 0 if not applicable or don't know: "))
        self.expenseUtilities = utilities_budget
        self.propExp[self.propId] += self.expenseUtilities


        insurance_budget = int(input("Please enter the estimated monthly insurance costs for the property. Enter 0 if not applicable or don't know: "))
        self.expenseInsurance = insurance_budget
        self.propExp[self.propId] += self.expenseInsurance


        hoa_budget = int(input("Please enter the estimated monthly HOA fees for the property. Enter 0 if not applicable or don't know: "))
        self.expenseHoa = hoa_budget
        self.propExp[self.propId] += self.expenseHoa


        lawn_care_budget = int(input("Please enter the estimated monthly budget for lawn care/snow removal for the property. Enter 0 if not applicable or don't know: "))
        self.expenseLawnCare = lawn_care_budget
        self.propExp[self.propId] += self.expenseLawnCare


        vacancy_budget = int(input("Please enter your estimated monthly budget for vacancies. Enter 0 if not applicable or don't know: "))
        self.expenseVacancy = vacancy_budget
        self.propExp[self.propId] += self.expenseLawnCare

    
        repairs_budget = int(input("Please enter your estimated monthly budget for repairs (i.e. small damages to property, such as holes in a wall, minor flooring repairs, paint touch-up, etc.). Enter 0 if not applicable or don't know: "))
        self.expenseRepairs = repairs_budget
        self.propExp[self.propId] += self.expenseRepairs


        cap_expenditure_budget = int(input("Please enter your estimated monthly budget for capital expenditures (i.e. high-cost items, such as a new roof, new appliances, new flooring, etc.). Enter 0 if not applicable or don't know: "))
        self.expenseCapExpenditures = cap_expenditure_budget
        self.propExp[self.propId] += self.expenseCapExpenditures
        

        property_mgmt_budget = int(input("Please enter your estimated monthly cost for property management. Enter 0 if not applicable or don't know: "))
        self.expensePropertyMgmt = property_mgmt_budget
        self.propExp[self.propId] += self.expenseCapExpenditures
        

        mortgage_budget = int(input("Please enter your estimated monthly mortgage amount. Enter 0 if not applicable or don't know: "))
        self.expenseMortgage = mortgage_budget
        self.propExp[self.propId] += self.expenseMortgage


        print(f"Property Expenses Dictionary: {self.propExp}")

    
    def calculateCashFlow(self):
        """
            calcCashFlow function/method
            will calculate cash flow using values from
            propInc and propExp dictionaries
        """
        C = {x: self.propInc[x] - self.propExp[x] for x in self.propInc if x in self.propExp}

        # for prop in self.propInc(key):
        #     self.propInc(key)

        #     print(f"Based on the information you provided, your monthly cash flow for {key} is estimated to be: {value}")


        for prop in self.propInc: 
            # print(f"\nWe calculate Cash Flow as projected income less projected expenses.\nBased on the information you provided, your estimated monthly cash flow for this property is: {C[self.propId]}\n")

            print(f"\nWe calculate Cash Flow as projected income less projected expenses.\nBased on the information you provided, your estimated monthly cash flow for {self.propId.title()} is: $",format(C[self.propId],",.2f"))



    def calculateInitialInvestment(self):
        print("\nFinally, we are going to calculate your initial investment (the amount you are putting in up-front for the purchase of the rental property). We will use this amount to calculate your ROI.")

        self.upFrontInvestment[self.propId] = 0

        purchase_price = int(input("What is the purchase price of the property? Enter a numerical value: "))
        self.purchasePrice = purchase_price
        self.upFrontInvestment[self.propId] += self.purchasePrice


        closing_costs = int(input("Please enter your estimated closing costs. Enter 0 if not applicable or don't know. Or enter an estimated amount of 3-5% of the purchase price: "))
        self.closingCosts = closing_costs
        self.upFrontInvestment[self.propId] += self.closingCosts


        down_payment = int(input("Please enter your down payment amount. Enter 0 if not applicable or don't know: "))
        self.downPayment = down_payment
        self.upFrontInvestment[self.propId] += self.downPayment


        rehab_budget = int(input("Please enter your rehab budget (i.e. painting the outside of the property, other cosmetic changes, or bigger changes such as fixing electrical/plumbing/roofing issues). Enter 0 if not applicable or don't know: "))
        self.rehabBudget = rehab_budget
        self.upFrontInvestment[self.propId] += self.rehabBudget



        other_misc_costs = int(input("Please enter the total amount of any other up-front investment costs you anticipate. Enter 0 if not applicable or don't know: "))
        self.otherMiscCosts = other_misc_costs
        self.upFrontInvestment[self.propId] += self.otherMiscCosts

        # self.downPayment = down_payment
        # if self.downPayment == 'calc':
        #     down_pmt_calced = self.purchasePrice * .015
        #     print(f"Your estimated down payment is {down_pmt_calced}.")
            # self.upFrontInvestment[self.propId] += down_pmt_calced

        # else:
        #     self.upFrontInvestment[self.propInc] += self.downPayment




    def calculateRoi(self):
        for prop in self.propInc: 
            print(f"\nWe calculate Cash Flow as projected income less projected expenses.\nBased on the information you provided, your estimated monthly cash flow for this property is: {C[self.propId]}")




rentalProp = Roi_Calc(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

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

run()




   
    


