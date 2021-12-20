# general


class APITesterException(Exception):
    pass


# get method


class APITesterGetDataException(APITesterException):
    pass


class APITesterGetException(APITesterException):
    pass


class APITesterGetJsonException(APITesterException):
    pass


# put method


class APITesterPutException(APITesterException):
    pass


# delete method


class APITesterDeleteException(APITesterException):
    pass


# put method


class APITesterPostException(APITesterException):
    pass


# head method


class APITesterHeadException(APITesterException):
    pass


# options method


class APITesterOptionsException(APITesterException):
    pass


# patch method


class APITesterPatchException(APITesterException):
    pass


# session method


class APITesterSessionException(APITesterException):
    pass


# execute


class APITesterExecuteException(APITesterException):
    pass


# json


class APITesterJsonException(APITesterException):
    pass


# xml


class APITesterXMLException(APITesterException):
    pass


class APITesterXMLTypeException(APITesterException):
    pass

# API data check


class APIStatusCodeException(APITesterException):
    pass


class APITextCodeException(APITesterException):
    pass


class APIContentCodeException(APITesterException):
    pass


class APIHeaderCodeException(APITesterException):
    pass


class APIHistoryCodeException(APITesterException):
    pass


class APIEncodingCodeException(APITesterException):
    pass


class APICookiesCodeException(APITesterException):
    pass


class APIElapsedCodeException(APITesterException):
    pass
