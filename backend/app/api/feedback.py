from typing import List
from ..crud import crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import models, schemas
from ..database.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.FeedbackCreate)
async def create_feedback(feedback: schemas.FeedbackCreate, db: AsyncSession = Depends(get_db)):
    if feedback.score < 1 or feedback.score > 5:
        raise HTTPException(status_code=400, detail="Score must be between 1 and 5")
    db_feedback = models.Feedback(score=feedback.score, comment=feedback.comment)
    try:
        return await crud.create_feedback(db, db_feedback)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Error saving feedback")

@router.get("/", response_model=List[schemas.FeedbackCreate])
async def get_all_feedbacks(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_feedback_entries(db)