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
        amount=loan_application_create.loan_amount_usd,
        term_months=loan_application_create.loan_length_months,
        annual_income=loan_application_create.annual_income_usd,
    )
    loan_applications.append(new_loan_application)
    return new_loan_application


@app.put("/loans/{loan_id}")
def update_loan_application(loan_id: int, updated_loan: LoanApplicationCreate):
    for loan_application in loan_applications:
        if loan_application.id == loan_id:
            loan_application.applicant_name = updated_loan.applicant_name
            loan_application.loan_amount_usd = updated_loan.loan_amount_usd
            loan_application.loan_length_months = updated_loan.loan_length_months
            loan_application.annual_income_usd = updated_loan.annual_income_usd
            break


@app.delete("/loans/{loan_id}")
def delete_loan_application(loan_id: int):
    for i, loan_application in enumerate(loan_applications):
        if loan_id == loan_application.id:
            loan_applications.pop(i)


@app.patch("/loans/{loan_id}")
def patch_loan_application(loan_id: int, key: str, value):
    try:
        loan_application = loan_applications[loan_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Loan not found")
    if key in ["loan_amount_usd", "annual_income_usd"]:
        setattr(loan_application, key, float(value))
    elif key == "applicant_name":
        setattr(loan_application, key, value)
    elif key == "loan_length_months":
        setattr(loan_application, key, int(value))
    else:
        raise HTTPException(status_code=404, detail="Key not found")
