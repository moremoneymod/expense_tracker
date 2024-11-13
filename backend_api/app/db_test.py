from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from backend_api.app.models import Base
from sqlalchemy import select
from models import Transaction
import asyncio

DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost:5432/postgres"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# Base.metadata.create_all(bind=engine)

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with AsyncSessionLocal as session:
        yield session


asyncio.run(main())
