from fastapi import FastAPI
from routers import users
from routers import auth, wallets, transfers, crypto, savings, insurance, scoring, credits, admin, notifications
app = FastAPI(title="Linc API v1.8")

app.include_router(auth.router)
app.include_router(wallets.router)
app.include_router(transfers.router)
app.include_router(crypto.router)
app.include_router(savings.router)
app.include_router(insurance.router)
app.include_router(scoring.router)
app.include_router(credits.router)
app.include_router(admin.router)
app.include_router(notifications.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Linc API v1.8 is live"}
