from feeder import DogFeeder
from fastapi import FastAPI

app = FastAPI()
feeder = DogFeeder(17, 4)


@app.get("/")
async def root():
    return {"message": "root page"}


@app.get("/status")
async def status():
    return {"message": feeder.status}


@app.post("/move_stepper")
async def move_stepper(steps: int = 0, delay: float = 0.5):
    feeder.drive_stepper(steps, delay)
    return {"Message": f"Moved stepper {steps} steps"}


def main():
    feeder.drive_stepper(3200, 1)


if __name__ == "__main__":
    main()
