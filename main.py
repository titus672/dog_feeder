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


def main():
    feeder.test_stepper(200, 5)


if __name__ == "__main__":
    main()
