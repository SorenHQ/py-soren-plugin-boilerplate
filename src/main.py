from fastapi  import FastAPI
from src.soren.protocolv1 import router as sorenInterface
app = FastAPI(
    title="Plugin Boilerplate",
    description="A FastAPI-based plugin for Soren Plugin",
    version="1.0.0",
    
)
app.include_router(prefix="/api",router=sorenInterface)



#Soren Version is Under Soren Protocol  , it is GETMethod and return Information's About Version of Itself and Soren Protocol
@app.get("/version")
async def intro():
    return   {
        "name": "pyCalc",
        "author": "soren-team",
        "version": "v8.7.1",
        "proto": "v0.0.1",
        "schema_version": "srn-schema-v1"
  }