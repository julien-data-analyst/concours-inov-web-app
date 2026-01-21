from pydantic import BaseModel

# Base schema with common attributes
class PublisherBase(BaseModel):
    name: str
    web_url: str = ""

class PublisherBase(BaseModel):
    name: str
    web_url: str = ""

# Schema for reading/returning an item (includes id)
class Publisher(PublisherBase):
    id: int

    class Config:
        orm_mode = True