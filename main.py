from fastapi import FastAPI, HTTPException
from storage import (
    loan_applications,
    get_loan_application,
    update_loan_application,
    pop_loan_application,
)
from model import LoanApplicationCreate, LoanApplication, LoanStatus

app = FastAPI()


@app.get("/loans")
def read_loan_applications():
    return loan_applications


@app.get("/loans/{loan_id}")
def read_loan_application(loan_id: int):
    if loan_application := get_loan_application(loan_id):
        return loan_application
    raise HTTPException(status_code=404, detail="Loan application not found")


@app.post("/loans/", status_code=201)
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
def put_loan_application(loan_id: int, updated_loan: LoanApplicationCreate):
    if loan_application := get_loan_application(loan_id):
        update_loan_application(loan_application, updated_loan)
        return loan_application
    raise HTTPException(status_code=404, detail="Loan application not found")


@app.patch("/loans/{loan_id}")
def patch_loan_application(loan_id: int, key: str, value):
    if loan_application := get_loan_application(loan_id):
        if key in ["loan_amount_usd", "annual_income_usd"]:
            setattr(loan_application, key, float(value))
        elif key == "applicant_name":
            setattr(loan_application, key, value)
        elif key == "loan_length_months":
            setattr(loan_application, key, int(value))
        elif key == "status":
            valid_status_changes = [(LoanStatus.SUBMITTED, LoanStatus.APPROVED), (LoanStatus.SUBMITTED, LoanStatus.DENIED)]
            try:
                status_change_attempt = (loan_application.status, LoanStatus(value))
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid status")
            if status_change_attempt in valid_status_changes:
                setattr(loan_application, key, value)
            else:
                raise HTTPException(status_code=400, detail="Invalid status change")
        else:
            raise HTTPException(status_code=400, detail="Key not found")
    else:
        raise HTTPException(status_code=404, detail="Loan application not found")


@app.delete("/loans/{loan_id}", status_code=204)
def delete_loan_application(loan_id: int):
    if pop_loan_application(loan_id):
        return
    raise HTTPException(status_code=404, detail="Loan application not found")
