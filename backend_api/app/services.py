import json

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend_api.app import models, schemas


async def db_get_all_transactions(db: AsyncSession):
    transaction_model = models.Transaction
    transactions = {}
    transactions["status_code"] = 200
    async with db() as session:
        result = await session.execute(select(transaction_model))
        transactions_data = result.scalars().all()
        if len(transactions_data) == 0:
            transactions["status_code"] = 404
        else:
            transactions["transactions"] = {}
        for transaction in transactions_data:
            transactions["transactions"][transaction.id] = {"amount": transaction.amount,
                                                            "category": transaction.category,
                                                            "date": transaction.date,
                                                            "description": transaction.description}
    response = json.dumps(transactions, ensure_ascii=False)
    print(transactions)
    return response


async def db_get_transaction_by_id(db: AsyncSession, transaction_id):
    transaction_model = models.Transaction
    response = {}
    response["status_code"] = 200
    async with db() as session:
        result = await session.execute(select(transaction_model).where(transaction_model.id == int(transaction_id)))
        transaction_data = result.scalars().all()
        if len(transaction_data) == 0:
            response["status_code"] = 404
        else:
            transaction_data = transaction_data[0]
            response["transactions"] = {}
            response["transactions"][transaction_id] = {"amount": transaction_data.amount,
                                                        "category": transaction_data.category,
                                                        "date": transaction_data.date,
                                                        "description": transaction_data.description}
    response = json.dumps(response, ensure_ascii=False)
    return response


async def db_create_transaction(db: AsyncSession, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    response = {}
    response["status_code"] = 200
    async with db() as session:
        try:
            session.add(db_transaction)
            await session.commit()
            await session.refresh(db_transaction)
        except:
            response["status_code"] = 500
    return response

async def db_update_transaction(db: AsyncSession, transaction: schemas.TransactionUpdate):
    updated_transaction = models.Transaction
