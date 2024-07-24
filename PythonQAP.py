import datetime

# Description: One Stop Insurance Company Policy Calculations
# Author: Nicole Sparkes
# Date: July 18,2024 - July

# Constants
DEFAULT_POLICY_NUMBER = 1944 # Starting Policy Number
BASIC_PREMIUM = 869.00
DISCOUNT = 0.25 # Discount for additional cars
EXTRA_LIABILITY_COST = 130.00 # Cost of additional libility per car
GLASS_COVERAGE_COST = 86.00 
LOANER_CAR_COST = 58.00
HST_Rate = 0.15
PROCESSING_FEE = 39.99

# Function to read constants from Const.dat file
def read_constants():
    with open("Const.dat", "r") as file:
        values = file.readline().split(',')
    return [float(value) for value in values]

# Function to validate the province input
def validate_province(province, valid_provinces_list):
    return province in valid_provinces_list

# Function for insurance policy calculations
def calculate_premium(num_cars, extra_liabilty, glass_coverage, loaner_car):
    base_cost = BASIC_PREMIUM + (num_cars -1) * (BASIC_PREMIUM * (1 - DISCOUNT))
    print(f"Base cost for {num_cars} cars: ${base_cost:.2f}")

    extra_cost = 0

    if extra_liabilty:
        extra_cost += EXTRA_LIABILITY_COST
        print(f"Added extra liability cost: ${EXTRA_LIABILITY_COST:.2f}")
    
    if glass_coverage:
        extra_cost += GLASS_COVERAGE_COST
        print(f"Added glass coverage cost: ${GLASS_COVERAGE_COST:.2f}")
    
    if loaner_car:
        extra_cost += LOANER_CAR_COST
        print(f"Added loaner car coverage cost: ${LOANER_CAR_COST:.2f}")
    
    total_premium_cost = base_cost + extra_cost
    print(f"Total premium cost (before HST): ${total_premium_cost:.2f}")

    hst = total_premium_cost * HST_Rate
    print(f"HST: ${hst:.2f}")

    total_insurance_cost = total_premium_cost + hst
    print(f"Total insurance cost including HST: ${total_insurance_cost}")

    return total_premium_cost, hst, total_insurance_cost

def handle_claims():
    # Predefined claims data
    claims = [
        ("1234", "2024-01-01", 500.00),
        ("6738", "2023-12-02", 750.00),
        ("2736", "2023-05-18", 1000.00)
    ]
    return claims

# Calculations for the first payment date (first day of the next month)
def get_first_payment_date():
    today = datetime.date.today()
    first_payment_date = (today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    return first_payment_date

# Main function to run the insurance policy calculations
def main():
    valid_provinces_list = ["NL", "PE", "ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NT", "YT", "NU"]

    policy_number = DEFAULT_POLICY_NUMBER

    # Call the get_first_payment_date() function to calculate the first payment date
    first_payment_date = get_first_payment_date()

    while True:
        first_name = input("Enter the customer's first name: ")
        last_name = input("Enter the customer's last name: ")
        address = input("Enter the customer's address: ")
        city = input("Enter the customer's city: ")

        province = input("Enter the customer's province (XX): ").upper()
        while not validate_province(province, valid_provinces_list):
            print("Invalid province code. Please enter a valid province.")
            province = input("Enter the customer's province (XX): ").upper()
        
        postal_code = input("Enter the customer's postal code: ")
        phone_number = input("Enter the customer's phone number: ")

        # Insurance details
        num_cars = int(input("Enter the number of cars: "))
        extra_liability = input("Would you like to add extra liability coverage? (Y/N):").upper() == 'Y'
        glass_coverage = input("Would you like to add glass coverage? (Y/N): ").upper() == 'Y'
        loaner_car = input("Would you like to add loaner car coverage? (Y/N): ").upper() == 'Y'

        payment_method = input("Enter the payment method (Full, Monthly, Down Payment):").title()
        while payment_method not in ['Full', 'Monthly', 'Down Payment']:
            payment_method = input("Invalid payment method. Please enter a valid payment method (Full, Monthly, Down Payment):").title()
        
        if payment_method == 'Down Payment':
            down_payment = float(input("Enter the down payment amount: "))
        
        claims = handle_claims()

        # Calculate the insurance premium
        base_cost = BASIC_PREMIUM + (num_cars - 1) * (BASIC_PREMIUM * (1 - DISCOUNT))
        print(f"Base cost for {num_cars} cars: ${base_cost:.2f}")

        extra_cost = 0

        if extra_liability:
            extra_cost += EXTRA_LIABILITY_COST
            print(f"Added extra liability cost: ${EXTRA_LIABILITY_COST:.2f}")
        
        if glass_coverage:
            extra_cost += GLASS_COVERAGE_COST
            print(f"Added glass coverage cost: ${GLASS_COVERAGE_COST:.2f}")

        if loaner_car:
            extra_cost += LOANER_CAR_COST
            print(f"Added loaner car coverage cost: ${LOANER_CAR_COST:.2f}")
        
        total_premium_cost = base_cost + extra_cost

        hst = total_premium_cost * HST_Rate
        print(f"HST: ${hst:.2f}")

        total_insurance_cost = total_premium_cost + hst
        print(f"Total insurance cost: ${total_insurance_cost:.2f}")

        # Calculate the payment details based on payment method
        if payment_method == 'Full':
            payment_due = total_insurance_cost # no additional processing fee
        elif payment_method == 'Monthly':
            monthly_payment = (total_insurance_cost + PROCESSING_FEE) / 8
            payment_due = monthly_payment
        elif payment_method == 'Down Payment':
            monthly_payment = (total_insurance_cost - down_payment + PROCESSING_FEE) / 8
            payment_due = monthly_payment
        
        # Display receipt with all the collected and calculated information
        print("\n" + "-" * 50)
        print("              INSURANCE POLICY RECEIPT              ")
        print("-" * 50)
        print("Customer Information:")
        print(f"    Name: {first_name} {last_name}")
        print(f"    Address: {address}")
        print(f"    City: {city}")
        print(f"    Province: {province}")
        print(f"    Postal Code: {postal_code}")
        print(f"    Phone: {phone_number}")
        print("-" * 50)
        print("Insurance Information:")
        print(f"    Number of Cars: {num_cars}")
        print(f"    Extra Liability: {'Yes' if extra_liability else 'No'}")
        print(f"    Glass Coverage: {'Yes' if glass_coverage else 'No'}")
        print(f"    Loaner Car: {'Yes' if loaner_car else 'No'}")
        print("-" * 50)
        print("Cost Breakdown:")
        print(f"    Basic Premium: ${BASIC_PREMIUM:.2f}")
        print(f"    Discount for Additional Cars: {BASIC_PREMIUM * DISCOUNT * (num_cars - 1):.2f}")
        if extra_liability:
            print(f"    Extra Liability Cost: ${EXTRA_LIABILITY_COST:.2f}")
        if glass_coverage:
            print(f"    Glass Coverage Cost: ${GLASS_COVERAGE_COST:.2f}")
        if loaner_car:
            print(f"    Loaner Car Cost: ${LOANER_CAR_COST:.2f}")
        print(f"    Total Premium Cost (before HST): ${total_premium_cost:.2f}")
        print(f"    HST: ${hst:.2f}")
        print(f"    Total Insurance Cost (including HST): ${total_insurance_cost:.2f}")
        print(f"    Payment Due: ${payment_due:.2f}")
        if payment_method != 'Full':
            print(f"    Monthly Payment: ${monthly_payment:.2f}")
            print(f"    First Payment Date: {first_payment_date}")
        print("-" * 50)
        print("Previous Claims:")
        print(f"  Claim Number   |   Claim Date   |   Claim Amount")
        print("-" * 50)
        for claim in claims:
            print(f"  {claim[0]:<12}   |   {claim[1]:<12}   |   ${claim[2]:.2f}")
        print("-" * 50)
        print(f"Thank you for choosing One Stop Insurance Company!")
        print("-" * 50)

        # Save data and update policy number
        with open('policies.txt', 'a') as file:
            file.write(f"{first_name},{last_name},{policy_number},{address},{city},{province},{postal_code},{phone_number},"
                       f"{num_cars},{extra_liability},{glass_coverage},{loaner_car},{total_insurance_cost:.2f},{payment_due:.2f},{payment_method},{datetime.datetime.now()}\n")
        
        print("\nSaving Policy Data. . .")
        policy_number += 1
        print(f"Policy data saved! Next policy number: {policy_number}")

        more_customers = input("Would you like to enter another customer? (Y/N):").upper()
        if more_customers == 'N':
            break
if __name__ == "__main__":
    main()