from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, RedirectResponse
from typing import Optional
import uvicorn

import sys
import json

sys.path.insert(0, "/var/fy_trade/")
# sys.path.insert(0,"/home/user/fyers-data-api/data_rest_fastapi")

# from fy_config.fy_data_external_functions import fy_getHistoricalOHLCV_V7, fy_getQuote, fy_getL2DataDepthBox
#
# from fy_config.fy_data_external_functions import *
# from fy_config.fy_base_success_error_codes import *
# from fy_config.fy_base_api_keys_values import *
# from fy_config.fy_base_success_error_messages import *
# from fy_config.fy_common_api_keys_values import *
# from fy_config.fy_data_and_trade_defines import *

from app.route import history, quotes, market_depth

app = FastAPI()

app.include_router(history.router, prefix='/data-rest/v2')
app.include_router(quotes.router, prefix='/data-rest/v2')
app.include_router(market_depth.router, prefix='/data-rest/v2')


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8080, reload=True)
# history({"symbol":"NSE:SBIN-EQ", "resolution":"240", "date_format":0, "range_from":"1621901846", "range_to":"1621963046", "cont_flag":1})
# history()
# pass
