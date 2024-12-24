from fastapi.middleware.cors import CORSMiddleware
from app import app


origins = [
    "http://localhost:5173",  # Allow requests from your SvelteKit frontend
    "http://127.0.0.1:5173",  # Allow requests from your SvelteKit frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow cookies if needed
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
