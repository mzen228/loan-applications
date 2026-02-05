from fastapi import FastAPI
from storage import loan_applications
from model import LoanApplicationCreate, LoanStatus
from datetime import datetime

app = FastAPI()


@app.get("/loans/{loan_application_id}")
def read_loan_application(loan_application_id: int):
    for loan_application in loan_applications:
        if loan_application_id == loan_application.get("id"):
            return loan_application
    return {"error": "Loan application not found"}


@app.post("/loans/{loan_id}")
def create_loan_application(loan_application: LoanApplicationCreate):
    new_loan_application = {
        "id": len(loan_applications),
        "name": loan_application.applicant_name,
        "amount": loan_application.amount,
        "annual_income": loan_application.annual_income,
        "term_months": loan_application.term_months,
        "status": LoanStatus.SUBMITTED,
        "created_at": datetime.utcnow(),
    }
    loan_applications.append(new_loan_application)
    return new_loan_application
