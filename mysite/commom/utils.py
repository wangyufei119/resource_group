import os


def pack_msg(status, error='', result=''):
    result = {
        'status': status,
        'result': result,
        'error': error,
    }
    return result


def format_data(key_list, params):
    result = {}
    for key in key_list:
        value = params.get(key, '')
        if value:
            result.update({key: value})
    return result
