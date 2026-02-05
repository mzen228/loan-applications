from datetime import datetime
from enum import Enum

from pydantic import BaseModel, conint


class LoanStatus(Enum):
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    DENIED = "denied"


class LoanApplicationCreate(BaseModel):
    applicant_name: str
    amount: float = 0
    annual_income: float
    term_months: conint(gt=0, lt=301)