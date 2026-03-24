from pydantic import BaseModel, Field


class LoanRequest(BaseModel):

    Gender: str = Field(..., example="Male")
    Married: str = Field(..., example="Yes")
    Dependents: str = Field(..., example="0")
    Education: str = Field(..., example="Graduate")
    Self_Employed: str = Field(..., example="No")

    ApplicantIncome: float = Field(..., example=5000)
    CoapplicantIncome: float = Field(..., example=0)
    LoanAmount: float = Field(..., example=150)
    Loan_Amount_Term: float = Field(..., example=360)
    Credit_History: float = Field(..., example=1)

    Property_Area: str = Field(..., example="Urban")