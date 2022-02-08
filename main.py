import fastapi as _fastapi
import uvicorn as _server


import src.users.routes.user_routes as _users

app = _fastapi.FastAPI()

app.include_router(_users.router)

@app.get("/")
def home():
    return {"message":"hello World"}

if __name__ == "__main__":
    _server.run("main:app", reload=True)
