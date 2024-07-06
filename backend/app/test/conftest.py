import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from  ..database.database import Base, get_test_database_url

@pytest.fixture(scope="session")
def engine():
    return create_async_engine(get_test_database_url())

@pytest.fixture(scope="function")
async def setup_database(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def db_session(setup_database, engine):
    async with AsyncSession(engine) as session:
        yield session
        