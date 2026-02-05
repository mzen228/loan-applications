loan_applications = []


def get_loan_application(loan_id: int):
    for loan_application in loan_applications:
        if loan_id == loan_application.id:
            return loan_application


def update_loan_application(old_loan, updated_loan):
    old_loan.applicant_name = updated_loan.applicant_name
    old_loan.loan_amount_usd = updated_loan.loan_amount_usd
    old_loan.loan_length_months = updated_loan.loan_length_months
    old_loan.annual_income_usd = updated_loan.annual_income_usd


def pop_loan_application(loan_id: int):
    for i, loan_application in enumerate(loan_applications):
        if loan_id == loan_application.id:
            loan_applications.pop(i)
            return True
