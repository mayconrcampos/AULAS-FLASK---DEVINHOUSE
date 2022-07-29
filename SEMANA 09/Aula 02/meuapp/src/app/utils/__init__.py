

def exist_key(request_json, list_keys):
    hasNotInRequest = []
    for data in list_keys:
        if data in request_json:
            return request_json
        hasNotInRequest.append(data)
    
    if len(hasNotInRequest) == 0:
        return request_json
    return None