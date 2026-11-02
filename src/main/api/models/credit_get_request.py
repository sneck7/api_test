from src.main.api.models.base_model import BaseModel


class CreditGetRequest(BaseModel):
    accountId: int
    amount: float
    termMonths: int