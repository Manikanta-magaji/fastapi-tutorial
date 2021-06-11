from fastapi import APIRouter
from fastapi import Request
from starlette.responses import JSONResponse

from pydantic import BaseModel
from typing import List, Union


router = APIRouter()


class HistoryResponse(BaseModel):
    s: str
    candles: List[List[Union[int, float]]]


@router.get("/history/", response_model=HistoryResponse)
def history(symbol: str, resolution: str, date_format: str, range_from: str, range_to: str, cont_flag: bool = None):
    print('abcdef')
    return {
        "s": "ok",
        "candles": [
            [
                100,
                274.9,
                277.2,
                274.4,
                276.9,
                2235225
            ],
            [
                1609473600,
                277.0,
                278.05,
                276.8,
                277.75,
                2111307
            ]
        ]
    }


    # inpParamList = ["symbol", "range_from", "range_to", "resolution", "cont_flag", "date_format"]
    # accessToken = request.headers.get('Authorization')
    # inputDict = {}
    # for eachIp in inpParamList:
    #     if eachIp in request.query_params:
    #         inputDict[eachIp] = request.query_params[eachIp]
    # inputDict["accessToken"] = accessToken
    # funcRet = fy_getHistoricalOHLCV_V7(inputDict)
    #
    # status = funcRet["statusCode"]
    # body = funcRet["body"]
    # return JSONResponse(body, status_code=status)

