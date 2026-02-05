loan_applications = []

def get_loan_application(loan_application_id: int):
    for loan_application in loan_applications:
        if loan_application_id == loan_application.id:
            return loan_application
