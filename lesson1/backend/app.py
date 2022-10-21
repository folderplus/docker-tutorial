from typing import Optional

from beanie import init_beanie, Document
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


class Greeting(Document):
    message: str


async def init():
    # Create Motor client
    client = AsyncIOMotorClient(
        "mongodb://admin-user:admin-password@mongo:27017"
    )

    # Initialize beanie with the Product document class and a database
    await init_beanie(database=client.admin, document_models=[Greeting])

app = FastAPI(on_startup=[init])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def create(name: str = "world"):
    message = Greeting(message=f"Hello {name}!")
    await message.save()
    return message

@app.get("/all")
async def get_all():
    greetings = await Greeting.find().to_list()
    return greetings