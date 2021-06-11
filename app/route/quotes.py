
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/quotes/")
def quotes(request: Request):
    inpParamList = ["symbols", "accessToken"]
    accessToken = request.headers.get('Authorization')
    inputDict = {}
    for eachIp in inpParamList:
        if eachIp in request.query_params:
            inputDict[eachIp] = request.query_params[eachIp]
    inputDict["accessToken"] = accessToken
    funcRet = fy_getQuote(inputDict)
    if funcRet["statusCode"] == -1:
        return RedirectResponse(json.dumps(funcRet))
    status = funcRet["statusCode"]
    body = funcRet["body"]
    return JSONResponse(body, status_code=status)
