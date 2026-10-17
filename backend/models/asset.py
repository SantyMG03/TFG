"""Modelo de activo financiero."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Asset(BaseModel):
    __tablename__ = "assets"

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )
    symbol: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    asset_type: Mapped[str] = mapped_column(String(50), nullable=False)  # stock, etf, option, future, cash
    isin: Mapped[str | None] = mapped_column(String(12), nullable=True, index=True)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)

    account: Mapped["Account"] = relationship("Account", back_populates="assets")
    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="asset"
    )
