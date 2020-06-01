import gc
import sys
from appfly import request
from appfly import response
from multiprocessing import Pool, Manager
from app.domain.face import FaceDomain
from app.domain.errors.NoFileProvidedError import NoFileProvided

def __error_factory(error, status):
    return response.factory(
        {
            'error': {
                'message': error.msg,
                'type': error.type
            }
        },
        status)

def __handdle_request():
    body = request.get_json()
    original = body.get('original', None)
    toCompare = body.get('toCompare', None)

    if original is None or toCompare is None:
        raise NoFileProvided()

    return FaceDomain(original, toCompare).handdle()

def route():
    try:
        pool = Pool()
        req_return = pool.apply_async(__handdle_request)
        req_return = req_return.get()
        pool.close()
        del pool
        gc.collect()
  
        return response.factory({
            'same_person': 1 - float(req_return),
        })

    except NoFileProvided as error:
        return __error_factory(error, status=400)

    except Exception as e:
        print('e.msg: {}'.format(e))
        return response.factory(
                {
                    'msg': "unknown error",
                    'type': 'unknown_error'
                 },
                 status=500)
