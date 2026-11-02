from src.main.api.models.base_model import BaseModel


class CreditGetResponse(BaseModel):
    id: int
    amount: float
    termMonths: int
    balance: float
    creditId: int