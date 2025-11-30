from pydantic import BaseModel

class Slug(BaseModel):
    slug: str
    url: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class CreateSlug(BaseModel):
    url: str