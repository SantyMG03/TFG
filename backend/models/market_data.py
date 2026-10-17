"""Modelo de datos de mercado (cotizaciones históricas)."""

from datetime import date
from decimal import Decimal

from sqlalchemy import Date, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class MarketData(BaseModel):
    __tablename__ = "market_data"
    __table_args__ = (
        UniqueConstraint("symbol", "date", name="uq_market_data_symbol_date"),
    )

    symbol: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    open: Mapped[Decimal | None] = mapped_column(Numeric(20, 8), nullable=True)
    high: Mapped[Decimal | None] = mapped_column(Numeric(20, 8), nullable=True)
    low: Mapped[Decimal | None] = mapped_column(Numeric(20, 8), nullable=True)
    close: Mapped[Decimal | None] = mapped_column(Numeric(20, 8), nullable=True)
    volume: Mapped[int | None] = mapped_column(nullable=True)
    dividend: Mapped[Decimal | None] = mapped_column(Numeric(20, 8), nullable=True)
