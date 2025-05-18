from fastapi import FastAPI, Request
from api.endpoints import router as router
from core.logger import setup_logging
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
import time
app = FastAPI(title="AI Text Service")
setup_logging()

# Rate limiter config
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Track uptime
start_time = time.time()

app.include_router(router, prefix="/api")

@app.get("/health")
@limiter.limit("10/minute")
async def health(request: Request):
    uptime = int(time.time() - start_time)
    return {"status": "ok", "uptime": uptime}