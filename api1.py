from fastapi import FastAPI
from zzzzz import main

app = FastAPI()

@app.get("/zxc")
def zxc():
    return main()

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run(app, host="127.0.0.1", port=8001)
    except KeyboardInterrupt:
        print()