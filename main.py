import math
import argparse


# input version 1 - Begin
def input_loan_principal():
    print("Enter the loan principal:")
    return int(input())


def input_monthly_payment():
    print("enter the monthly payment:")
    return int(input())


def input_loan_interest():
    print("Enter the loan interest:")
    return float(input())


def input_number_periods():
    print("Enter the number of periods:")
    return int(input())
# input version 1 - End


def calculate_nominal_interest_rate(number_loan_interest):
    return number_loan_interest / 1200


def check_user_arguments():
    flag = True
    result = list()

    if args.type != "annuity" and args.type != "diff":
        flag = False
    elif args.type == "annuity":
        if (args.payment is not None or args.principal is None or args.periods is None) \
                and (args.payment is None or args.principal is not None or args.periods is None) \
                and (args.payment is None or args.principal is None or args.periods is not None) \
                or args.interest is None:
            flag = False
        elif args.payment is None and args.principal is not None and args.periods is not None and args.interest is not None:
            flag = False if int(args.principal) < 0 or int(args.periods) < 0 or float(args.interest) < 0 else True
            annuity_type = "annuity monthly payment amount"
        elif args.payment is not None and args.principal is None and args.periods is not None and args.interest is not None:
            flag = False if int(args.payment) < 0 or int(args.periods) < 0 or float(args.interest) < 0 else True
            annuity_type = "the monthly payment"
        elif args.payment is not None and args.principal is not None and args.periods is None and args.interest is not None:
            flag = False if int(args.payment) < 0 or int(args.principal) < 0 or float(args.interest) < 0 else True
            annuity_type = "number of monthly payments"
    elif args.type == "diff":
        if args.payment is not None or args.principal is None or args.periods is None or args.interest is None:
            flag = False
        elif int(args.principal) < 0 or int(args.periods) < 0 or float(args.interest) < 0:
            flag = False

    if not flag:
        print("Incorrect parameters")

    result.append(flag)
    if args.type == "annuity" and flag:
        result.append(annuity_type)

    return result


# input version 1 - Begin
# print("""What do you want to calculate?
# type "n" - for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" - for the monthly payment""")
# type_calculate = input()

# if type_calculate == "n":
#     loan_principal = input_loan_principal()
#     monthly_payment = input_monthly_payment()
#     loan_interest = input_loan_interest()

#     nominal_interest_rate = calculate_nominal_interest_rate(loan_interest)
#     number_monthly_payments = math.ceil(math.log(monthly_payment / (monthly_payment
#                                                                     - nominal_interest_rate * loan_principal),  1 + nominal_interest_rate))
#     print(f"It will take {number_monthly_payments // 12} years and {number_monthly_payments % 12} months to repay this loan!")
# elif type_calculate == "a":

#     loan_principal = input_loan_principal()
#     number_of_periods = input_number_periods()
#     loan_interest = input_loan_interest()

#     nominal_interest_rate = calculate_nominal_interest_rate(loan_interest)
#     annuity_monthly_payment = math.ceil(loan_principal * (nominal_interest_rate
#                                                           * math.pow(1 + nominal_interest_rate, number_of_periods)
#                                                           / (math.pow(1 + nominal_interest_rate, number_of_periods) - 1)))
#     print(f"Your monthly payment = {annuity_monthly_payment}!")
# else:
#     print("Enter the annuity payment:")
#     annuity_payment = float(input())
#     number_of_periods = input_number_periods()
#     loan_interest = input_loan_interest()

#     nominal_interest_rate = calculate_nominal_interest_rate(loan_interest)
#     loan_principal = round(annuity_payment / (nominal_interest_rate
#                                              * math.pow(1 + nominal_interest_rate, number_of_periods)
#                                               / (math.pow(1 + nominal_interest_rate, number_of_periods) - 1)))
#     print(f"Your loan principal = {loan_principal}!")
#  input version 1 - End


#  input version 2 - Begin
parser = argparse.ArgumentParser()

parser.add_argument("--type", help="You need to select only one type of payment calculation: annuity or diff")
parser.add_argument("--payment", help="Monthly payment amount")
parser.add_argument("--principal", help="Loan principal")
parser.add_argument("--periods", help="the number of months required to repay the loan")
parser.add_argument("--interest")

args = parser.parse_args()
check_input = check_user_arguments()

if check_input[0]:
    if args.type == "annuity" and check_input[1] == "annuity monthly payment amount":
        nominal_interest_rate = calculate_nominal_interest_rate(float(args.interest))
        annuity_monthly_payment = math.ceil(int(args.principal) * (nominal_interest_rate
                                                           * math.pow(1 + nominal_interest_rate, int(args.periods))
                                                           / (math.pow(1 + nominal_interest_rate, int(args.periods)) - 1)))
        print(f"Your annuity payment = {annuity_monthly_payment}!")
        print(f"Overpayment = {int(args.periods) * annuity_monthly_payment - int(args.principal)}")

    if args.type == "annuity" and check_input[1] == "the monthly payment":
        nominal_interest_rate = calculate_nominal_interest_rate(float(args.interest))
        loan_principal = math.floor(int(args.payment) / (nominal_interest_rate
                                            * math.pow(1 + nominal_interest_rate, int(args.periods))
                                            / (math.pow(1 + nominal_interest_rate, int(args.periods)) - 1)))
        print(f"Your loan principal = {loan_principal}!")
        print(f"Overpayment = {int(args.periods) * int(args.payment) - loan_principal}")

    if args.type == "annuity" and check_input[1] == "number of monthly payments":
        nominal_interest_rate = calculate_nominal_interest_rate(float(args.interest))
        number_monthly_payments = math.ceil(math.log(int(args.payment) / (int(args.payment)
                                                                    - nominal_interest_rate * int(args.principal)),  1 + nominal_interest_rate))
        print(f"It will take {number_monthly_payments // 12} years "
              + (f"and {number_monthly_payments % 12} months" if number_monthly_payments % 12 != 0 else "")
              + "to repay this loan!")
        print(f"Overpayment = {number_monthly_payments * int(args.payment) - int(args.principal)}")

    if args.type == "diff":
        nominal_interest_rate = calculate_nominal_interest_rate(float(args.interest))
        sum_repayment_months = 0
        for current_repayment_month in range(1, int(args.periods) + 1):
            differentiated_payment = math.ceil(int(args.principal) / int(args.periods) + nominal_interest_rate * (int(args.principal) - int(args.principal) * ((current_repayment_month - 1) / int(args.periods))))
            sum_repayment_months += differentiated_payment
            print(f"Month {current_repayment_month}: payment is {differentiated_payment}")

        print()
        print(f"Overpayment = {sum_repayment_months - int(args.principal)}")
# input version 2 - End
