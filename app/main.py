from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.v1 import bike

from app.core.config import settings
from app.core.vapaus_exception import VapausException

from app.api.deps import populate_organizations
from app.api.deps import populate_bikes


populate_organizations()
populate_bikes()


app = FastAPI(title=settings.PROJECT_NAME)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(VapausException)
async def vapaus_exception_handler(request, exception: VapausException):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "errors": [
                {"error_message": exception.error_message, "error_code": exception.error_code}
            ]
        },
    )


api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(bike.router)

app.include_router(api_v1_router)
