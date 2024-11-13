from fastapi import APIRouter, HTTPException
# from backend_api.app.services import get_transaction
from backend_api.app.schemas import TransactionCreate, TransactionUpdate, TransactionResponse
import asyncio
from backend_api.app.services import db_create_transaction, db_get_all_transactions, db_get_transaction_by_id
from backend_api.app.database import AsyncSessionLocal

router = APIRouter(tags=["transactions"])


@router.get("/transactions")
async def get_transactions():
    transactions = await db_get_all_transactions(AsyncSessionLocal)
    return transactions


@router.get("/transactions/{transaction_id}")
async def get_transaction_by_id(transaction_id):
    response = await db_get_transaction_by_id(AsyncSessionLocal, transaction_id)
    return response


@router.post("/transactions")
async def create_transaction(transaction: TransactionCreate):
    response = await db_create_transaction(AsyncSessionLocal, transaction)
    print(response)
    return response


@router.put("/transactions/{transaction_id}")
async def update_transaction(transaction: TransactionUpdate):
    print(transaction)
    return transaction


@router.delete("/transactions/{transaction_id}")
async def delete_transaction(transaction_id: int):
    pass
