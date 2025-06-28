from fastapi import FastAPI
from app.routers.tasks import router as task_router
app = FastAPI()

app.include_router(task_router)

@app.get('/hello_world')
async def hello():
    return {'Message': 'Hellow World'}