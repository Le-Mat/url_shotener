from fastapi import APIRouter

from urlshortener.services.slug import generate_slug

router = APIRouter()

# Get a slug
@router.get("/slug")
def get_slug():
    return {"slug": generate_slug()}

# Create a slug
@router.post("/slug")
def create_slug(slug: str):
    return {"slug": slug}

# Delete a slug
@router.delete("/slug")
def delete_slug(slug: str):
    return {"slug": slug}
