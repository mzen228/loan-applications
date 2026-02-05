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

    def __init__(self, applicant_name: str, amount: float, term_months: int):
        self.id = LoanApplication.ID
        self.status = LoanStatus.SUBMITTED
        self.created_at = datetime.utcnow()
        self.applicant_name = applicant_name
        self.amount = amount
        self.term_months = term_months

        LoanApplication.ID += 1


class LoanApplicationCreate(BaseModel):
    applicant_name: str
    amount: float = 0
    annual_income: float
    term_months: conint(gt=0, lt=301)
