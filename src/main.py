import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager

sys.path.append(str(Path(__file__).parent.parent))


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    yield


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
