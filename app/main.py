from fastapi import FastAPI

app = FastAPI()

@app.get('/hello_world')
async def hello():
    return {'Message': 'Hellow World'}