import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

def get_database_url():
    return os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:root@db/feedback_app")

def get_test_database_url():
    return os.getenv("TEST_DATABASE_URL", "postgresql+asyncpg://postgres:root@test_db/feedback_app_test")

# Use get_database_url() for the main engine
engine = create_async_engine(get_database_url(), echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Create a separate engine for testing
test_engine = create_async_engine(get_test_database_url(), echo=True)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine, class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session

async def get_test_db():
    async with TestSessionLocal() as session:
        yield session