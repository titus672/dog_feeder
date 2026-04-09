from feeder import DogFeeder
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
feeder = DogFeeder(17, 4)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class MovementInput(BaseModel):
    steps: int
    delay: float


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/status")
async def status():
    return {"message": feeder.status}


@app.post("/move_stepper")
async def move_stepper(input: MovementInput):
    feeder.drive_stepper(input.steps, input.delay)
    return {"Message": f"Moved stepper {input.steps} steps"}


def main():
    feeder.drive_stepper(3200, 1)


if __name__ == "__main__":
    main()
