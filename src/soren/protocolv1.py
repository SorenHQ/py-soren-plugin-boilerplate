from typing import Any, Dict
from fastapi import APIRouter
from src.actions import actions
from src.attributes import attrs
from fastapi import HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/methods")
def methodList():
    la=[actions[el]().whoami() for el in actions]
    return JSONResponse(content={"data":la,"error":None})


@router.get("/attributes")
def attributeList():
    la=[attrs[el]().whoami() for el in attrs]
    return JSONResponse(content={"data":la,"error":None})

@router.get("/method/{name}")
def getMethodParams(name:str):
    try:
        return JSONResponse(content={"data":actions[name]().getParams(),"error":None})
    except Exception as e:     
        return HTTPException(status_code=404, content=dict({"code":404,"message":"method not found",})) 


@router.post("/method/{name}")
def runMethod(name:str, data: Dict[str, Any]):

    try:
        method = actions[name]()
        if hasattr(method, "long_running_process"):# 
            """
            For long-running processes under the Soren Protocol,
            a JobId key should be added to the response header. The action will then run asynchronously.
            Upon task registration, the response will include the `soren-job-id` header.
            Subsequently, encountering this header will halt the current workflow, placing it in observer mode, 
            where it awaits job completion notification via the Soren platform's event channel.
            """
            return  JSONResponse(content={"data":method.run(data),"error":None},headers=({"soren-job-id":method.getJobId()}))
        else:
            return JSONResponse(content={"data":method.run(data),"error":None})
    except Exception as e:     
        return JSONResponse(status_code=404, content=dict({"code":404,"message":"method not found","error":e.args})) 



@router.get("/attributes/{name}")
def getSettingsParams(attrname:str):
    try:
        return JSONResponse(content={"data":attrs[attrname]().getParams(),"error":None})
    except Exception as e:     
        return HTTPException(status_code=404, content=dict({"code":404,"message":"settings not found",})) 


@router.post("/attributes/{name}")
def setSettings(attrname:str,data:Dict[str, Any]):
    try:
        return JSONResponse(content={"data":attrs[attrname]().run(data),"error":None})
    except Exception as e:     
        return JSONResponse(status_code=404, content=dict({"code":404,"message":"method not found","error":e.args})) 