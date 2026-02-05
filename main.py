from fastapi import FastAPI
from storage import loan_applications
from model import LoanApplicationCreate, LoanApplication

app = FastAPI()


@app.get("/loans/{loan_application_id}")
def read_loan_application(loan_application_id: int):
    for loan_application in loan_applications:
        if loan_application_id == loan_application.id:
            return loan_application
    return {"error": "Loan application not found"}


@app.post("/loans/{loan_id}")
def create_loan_application(loan_application_create: LoanApplicationCreate):
    new_loan_application = LoanApplication(
        applicant_name=loan_application_create.applicant_name,
        amount=loan_application_create.amount,
        term_months=loan_application_create.term_months,
    )
    loan_applications.append(new_loan_application)
    return new_loan_application
