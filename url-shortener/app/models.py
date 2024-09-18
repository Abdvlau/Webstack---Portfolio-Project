from pydantic import BaseModel, AnyUrl
from datetime import datetime
from typing import Optional

class Url(BaseModel):
    short_url: str
    original_url: AnyUrl
    created_at: datetime = datetime.utcnow()
    clicks: int = 0