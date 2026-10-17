"""Modelo de cuenta de inversión."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Account(BaseModel):
    __tablename__ = "accounts"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)  # EUR, USD, GBP
    broker: Mapped[str] = mapped_column(String(100), nullable=False)  # interactive_brokers, trade_republic, ...
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="accounts")
    assets: Mapped[list["Asset"]] = relationship(
        "Asset", back_populates="account", cascade="all, delete-orphan"
    )
    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="account", cascade="all, delete-orphan"
    )
