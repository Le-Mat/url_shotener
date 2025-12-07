from pydantic import BaseModel

class Slug(BaseModel):
    slug: str
    url: str

class CreateSlug(BaseModel):
    url: str