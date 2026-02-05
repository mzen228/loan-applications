from datetime import datetime
from enum import Enum

from pydantic import BaseModel, conint


class LoanStatus(Enum):
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    DENIED = "denied"


class LoanApplication:
    ID = 0

    def __init__(
        self, applicant_name: str, amount: float, term_months: int, annual_income: int
    ):
        self.id = LoanApplication.ID
        self.status = LoanStatus.SUBMITTED
        self.created_at = datetime.utcnow()
        self.applicant_name = applicant_name
        self.loan_amount_usd = amount
        self.loan_length_months = term_months
        self.annual_income_usd = annual_income

        LoanApplication.ID += 1


class LoanApplicationCreate(BaseModel):
    applicant_name: str
    loan_amount_usd: float = 0
    annual_income_usd: float
    loan_length_months: conint(gt=0, lt=301)
