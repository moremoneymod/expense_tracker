from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Сумма операции")
    category_id: int
    category: str = Field(default="Покупка в офлайн магазине")
    date: str = Field(default=str(datetime.now()))
    description: Optional[str] = Field(max_length=255, default="Покупка в магазине")


class TransactionUpdate(BaseModel):
    amount: float = Field(None, gt=0, description="Сумма операции")
    category_id: int
    date: datetime
    description: Optional[str] = Field(max_length=255, default="Покупка в магазине")


class TransactionResponse(BaseModel):
    transaction_id: int
    amount: float
    category_id: int
    category: str
    date: str
    description: Optional[str]


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Название категории")


class CategoryResponse(BaseModel):
    category_id: int
    name: str


class BudgetCreate(BaseModel):
    category_id: int
    amount: float = Field(..., gt=0, description="Лимит бюджета")
    start_date: datetime
    end_date: datetime


class BudgetResponse(BaseModel):
    budget_id: int
    category_id: int
    amount: float
    start_date: datetime
    end_date: datetime