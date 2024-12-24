from fastapi import FastAPI, status
from .routers import posts, topics

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)  # Alternative path
async def health_check():
    return {"status": "ok"}


app.include_router(posts.router)
app.include_router(topics.router)

