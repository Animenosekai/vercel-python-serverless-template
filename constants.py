from flask import request, Response
from json import dumps

def makeResponse(data=None, error=None, code=200, cache_hit=False):
    """
    Shapes the response
    """
    if error is not None:
        responseBody = {"success": False, "error": error, "data": None}
    else:
        responseBody = {"success": True, "error": None, "data": data}

    if "minify" in request.values:
        response = Response(dumps(responseBody, ensure_ascii=False, separators=(",", ":")))
    else:
        response = Response(dumps(responseBody, ensure_ascii=False, indent=4))
    
    response.headers["Server"] = "Anise"
    response.headers["Content-Type"] = "application/json"
    """
    if cache_hit:
        response.headers["X-ANISE-CACHE"] = "HIT"
    else:
        response.headers["X-ANISE-CACHE"] = "MISS"
    """
    response.status_code = int(code)
    return response
