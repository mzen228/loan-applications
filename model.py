from enum import Enum

from pydantic import BaseModel


class LoanStatus(Enum):
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    DENIED = "denied"


class LoanApplication(BaseModel):
    applicant_name: str
    amount: float
    annual_income: float
    status: LoanStatus
