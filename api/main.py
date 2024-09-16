import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def oi_eu_sou_programador() -> str:
    
    return "Oi, eu sou programador!"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
    


