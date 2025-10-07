from .logger import logger
from fastapi import Request
import time


async def log_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "process_time": round(process_time, 4),
    }
    logger.info(log_dict)

    return response
