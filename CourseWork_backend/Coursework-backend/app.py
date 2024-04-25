from fastapi import FastAPI, BackgroundTasks

from email import send_email_background

app = FastAPI()


@app.get("/contact-us")
def contact_us(background_tasks: BackgroundTasks):
    send_email_background(
        background_tasks,
        "Hello World",
        "someemail@gmail.com",
        {"title": "Hello World", "name": "John Doe"},
    )
    return {"message": "Success"}
