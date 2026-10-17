"""Modelo de transacción / movimiento de cartera."""

from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Transaction(BaseModel):
    __tablename__ = "transactions"

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )
    asset_id: Mapped[int | None] = mapped_column(
        ForeignKey("assets.id", ondelete="SET NULL"), nullable=True
    )
    transaction_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # buy, sell, dividend, commission, split, transfer, deposit, withdrawal
    quantity: Mapped[Decimal | None] = mapped_column(Numeric(20, 8), nullable=True)
    price: Mapped[Decimal | None] = mapped_column(Numeric(20, 8), nullable=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(20, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    transaction_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    settlement_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    fee: Mapped[Decimal | None] = mapped_column(Numeric(20, 2), nullable=True)
    isin: Mapped[str | None] = mapped_column(String(12), nullable=True)
    notes: Mapped[str | None] = mapped_column(String(500), nullable=True)

    account: Mapped["Account"] = relationship("Account", back_populates="transactions")
    asset: Mapped["Asset | None"] = relationship("Asset", back_populates="transactions")
