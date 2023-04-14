from pydantic import BaseModel, PositiveFloat, Field
from datetime import datetime


class ReadingRequest(BaseModel):
    id: str
    temperature: PositiveFloat
    

class ReadingOut(BaseModel):
    id: str
    temperature: PositiveFloat
    timestamp: datetime = Field(default_factory=datetime.now)
