from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models.models import Feedback

async def create_feedback(db: AsyncSession, feedback: Feedback):
    db.add(feedback)
    await db.commit()
    await db.refresh(feedback)
    return feedback

async def get_all_feedback_entries(db: AsyncSession):
    stmt = select(Feedback).order_by(Feedback.id.desc())
    result = await db.execute(stmt)
    return result.scalars().all()