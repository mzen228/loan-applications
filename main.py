from fastapi import FastAPI, HTTPException
from storage import loan_applications
from model import LoanApplicationCreate, LoanApplication

app = FastAPI()


@app.get("/loans/{loan_application_id}")
def read_loan_application(loan_application_id: int):
    for loan_application in loan_applications:
        if loan_application_id == loan_application.id:
            return loan_application
    raise HTTPException(status_code=404, detail="Loan application not found")


@app.get("/loans")
def read_loan_applications():
    return loan_applications


@app.post("/loans/{loan_id}", status_code=201)
def create_loan_application(loan_application_create: LoanApplicationCreate):
    new_loan_application = LoanApplication(
        applicant_name=loan_application_create.applicant_name,
        amount=loan_application_create.amount,
        term_months=loan_application_create.term_months,
        annual_income=loan_application_create.annual_income,
    )
    loan_applications.append(new_loan_application)
    return new_loan_application

@app.put("/loans/{loan_id}")
def update_loan_application(loan_id: int, updated_loan: LoanApplicationCreate):
    for loan_application in loan_applications:
        if loan_application.id == loan_id:
            loan_application.applicant_name = updated_loan.applicant_name
            loan_application.amount = updated_loan.amount
            loan_application.term_months = updated_loan.term_months
            loan_application.annual_income = updated_loan.annual_income
            break