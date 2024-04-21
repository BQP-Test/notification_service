from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from twilio.rest import Client
from .utils import send_new_post, send_new_comment
from typing import List
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PayloadData(BaseModel):
    receiver_email: List
    article_id: str


# Example endpoint to send WhatsApp message
@app.post("/send-email-new-post/")
async def send_new_post_email(data: PayloadData):
    try:
        send_new_post(data.receiver_email, data.article_id)
        return {"messge":"Email Sent Success"}
    except:
        return JSONResponse(
            status_code=500,
            content={"message": "Failed to send email", "error": str(e)}
        )
        

@app.post("/send-email-new-comment/")
async def send_new_comment_email(data: PayloadData):
    try:
        send_new_comment(data.receiver_email, data.article_id)
        return {"messge":"Email Sent Success"}
    except:
        return JSONResponse(
            status_code=500,
            content={"message": "Failed to send email", "error": str(e)}
        )
        