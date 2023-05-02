from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from faker import Faker

# uvicorn main:app --reload

app = FastAPI()
fake = Faker()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    email: str


@app.get("/data")
async def get_data():
    return {"message": "Hello FastAPI"}


@app.post("/data")
def main(user: User):
    return user


@app.get("/name")
async def get_name():
    return {"name": fake.name()}


@app.get("/job")
async def get_job():
    return {"job": fake.job()}


@app.get("/posts")
async def get_posts():
    return {"posts": fake.pyint(min_value=0, max_value=99)}


@app.get("/likes")
async def get_likes():
    return {"likes": fake.pyint(min_value=1000, max_value=9999)}


@app.get("/followers")
async def get_followers():
    return {"followers": fake.pyint(min_value=100, max_value=999)}
