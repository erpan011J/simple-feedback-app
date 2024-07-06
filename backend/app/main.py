from .app_config import app
from .api import feedback

app.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
