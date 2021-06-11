
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/depth/")
def marketDepth(request: Request):
    returnDict = {"s": "error", "code": 400, "message": "Invalid Method"}
    paramsList = ["symbol", "ohlcv_flag"]
    inputDict = {}
    status = 400
    body = returnDict

    accessToken = request.headers.get('Authorization')
    if request.method == "GET":
        for i in paramsList:
            if i in request.query_params:
                inputDict[i] = request.query_params[i]
    inputDict["accessToken"] = accessToken
    funcRet = fy_getL2DataDepthBox(inputDict)
    if funcRet["statusCode"] == -1:
        return RedirectResponse(json.dumps(funcRet))
    elif request.method == "OPTIONS":
        response = RedirectResponse()
        response["Access-Control-Allow-Methods"] = "GET,OPTIONS"
        return response
    status = funcRet["statusCode"]
    body = funcRet["body"]
    return JSONResponse(body, status_code=status)
