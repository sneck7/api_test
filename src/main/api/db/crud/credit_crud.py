from sqlalchemy.orm import Session

from src.main.api.db.models.credit import Credit


class CreditCrudDB:

    @staticmethod
    def get_credit_by_account_id(db: Session, account_id: int):
        return db.query(Credit).filter_by(account_id=account_id).first()

