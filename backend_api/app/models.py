from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped
from typing import List


class Base(DeclarativeBase):
    pass


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    date: Mapped[str] = mapped_column(String)
