from pydantic import BaseModel


class LoanApplication(BaseModel):
    applicant_name: str
    amount: float
    annual_income: float
