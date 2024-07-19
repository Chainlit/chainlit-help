from fastapi import FastAPI
from chainlit.utils import mount_chainlit
from chainlit.context import init_http_context
import chainlit as cl
from app import main
import os, json

app = FastAPI()

prompt_path = os.path.join(os.getcwd(), "app/prompts/rag.json")


@app.get("/app/{message}")
async def read_main(message: str):
    init_http_context()
    with open(prompt_path, "r") as f:
        rag_prompt = json.load(f)
        settings = rag_prompt["settings"]
        del settings["provider"]
        cl.user_session.set("messages", rag_prompt["template_messages"])
        cl.user_session.set("settings", settings)
        cl.user_session.set("tools", rag_prompt["tools"])

    return {"answer": await main(cl.Message(message))}


mount_chainlit(app=app, target="app/app.py", path="/chainlit")
