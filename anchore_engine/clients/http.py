import json
import urllib3
import requests

http = urllib3.PoolManager()

def fpost(url, **kwargs):
    return(fpost_req(url, **kwargs))

def fget(url, **kwargs):
    return(fget_req(url, **kwargs))

def fput(url, **kwargs):
    return(fput_req(url, **kwargs))

def fdelete(url, **kwargs):
    return(fdelete_req(url, **kwargs))

def fpost_urllib(url, **kwargs):
    global http
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        try:
            headers = kwargs['headers']
        except:
            headers = {}
        try:
            aheader = urllib3.util.make_headers(basic_auth=':'.join(kwargs['auth']))
            headers.update(aheader)
        except:
            pass
        try:
            payload = kwargs['data']
        except:
            payload = None
        
        r = http.request('POST', url, headers=headers, body=payload)
        httpcode = r.status
        rawdata = r.data

        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)

    return(httpcode, jsondata, rawdata)

def fpost_req(url, **kwargs):
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        r = requests.post(url, stream=True, **kwargs)
        httpcode = r.status_code
        rawdata = ""
        for rchunk in r.iter_content(8192*100):
            rawdata = rawdata + rchunk

        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)
    return(httpcode, jsondata, rawdata)

def fput_urllib(url, **kwargs):
    global http
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        try:
            headers = kwargs['headers']
        except:
            headers = {}
        try:
            aheader = urllib3.util.make_headers(basic_auth=':'.join(kwargs['auth']))
            headers.update(aheader)
        except:
            pass
        try:
            payload = kwargs['data']
        except:
            payload = None
        
        r = http.request('PUT', url, headers=headers, body=payload)
        httpcode = r.status
        rawdata = r.data

        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)

    return(httpcode, jsondata, rawdata)

def fput_req(url, **kwargs):
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        r = requests.put(url, stream=True, **kwargs)
        httpcode = r.status_code
        rawdata = ""
        for rchunk in r.iter_content(8192*100):
            rawdata = rawdata + rchunk

        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)
    return(httpcode, jsondata, rawdata)

def fget_urllib(url, **kwargs):
    global http
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        try:
            headers = kwargs['headers']
        except:
            headers = {}
        try:
            aheader = urllib3.util.make_headers(basic_auth=':'.join(kwargs['auth']))
            headers.update(aheader)
        except:
            pass
        try:
            payload = kwargs['data']
        except:
            payload = None
        
        r = http.request('GET', url, headers=headers, body=payload)
        httpcode = r.status
        rawdata = r.data

        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)

    return(httpcode, jsondata, rawdata)

def fget_req(url, **kwargs):
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        r = requests.get(url, stream=True, **kwargs)
        httpcode = r.status_code
        rawdata = ""
        for rchunk in r.iter_content(8192*100):
            rawdata = rawdata + rchunk

        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)

    return(httpcode, jsondata, rawdata)

def fdelete_urllib(url, **kwargs):
    global http
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        try:
            headers = kwargs['headers']
        except:
            headers = {}
        try:
            aheader = urllib3.util.make_headers(basic_auth=':'.join(kwargs['auth']))
            headers.update(aheader)
        except:
            pass
        try:
            payload = kwargs['data']
        except:
            payload = None
        
        r = http.request('DELETE', url, headers=headers, body=payload)
        httpcode = r.status
        rawdata = r.data

        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)

    return(httpcode, jsondata, rawdata)

def fdelete_req(url, **kwargs):
    httpcode = 500
    rawdata = ""
    jsondata = {}
    try:
        r = requests.delete(url, stream=True, **kwargs)
        httpcode = r.status_code
        rawdata = ""
        for rchunk in r.iter_content(8192*100):
            rawdata = rawdata + rchunk
        #rawdata = r.text
        try:
            jsondata = json.loads(rawdata)
        except:
            jsondata = {}
    except Exception as err:
        rawdata = str(err)
    return(httpcode, jsondata, rawdata)

def anchy_get(url, raw=False, **kwargs):
    ret = True

    (httpcode, jsondata, rawdata) = fget(url, **kwargs)
    if httpcode == 200:
        if raw:
            ret = rawdata
        else:
            if jsondata != None:
                ret = jsondata
            elif rawdata:
                ret = rawdata
            else:
                ret = True
    else:
        e = Exception("failed get url="+str(url))
        e.__dict__.update({'httpcode':httpcode, 'anchore_error_raw':str(rawdata), 'anchore_error_json':jsondata})
        raise e

    return(ret)

def anchy_post(url, raw=False, **kwargs):
    ret = True

    (httpcode, jsondata, rawdata) = fpost(url, **kwargs)
    if httpcode == 200:
        if raw:
            ret = rawdata
        else:
            if jsondata != None:
                ret = jsondata
            elif rawdata:
                ret = rawdata
            else:
                ret = True
    else:
        e = Exception("failed post url="+str(url))
        e.__dict__.update({'httpcode':httpcode, 'anchore_error_raw':str(rawdata), 'anchore_error_json':jsondata})
        raise e

    return(ret)


def anchy_put(url, raw=False, **kwargs):
    ret = True

    (httpcode, jsondata, rawdata) = fput(url, **kwargs)
    if httpcode == 200:
        if raw:
            ret = rawdata
        else:
            if jsondata != None:
                ret = jsondata
            elif rawdata:
                ret = rawdata
            else:
                ret = True
    else:
        e = Exception("failed put url="+str(url))
        e.__dict__.update({'httpcode':httpcode, 'anchore_error_raw':str(rawdata), 'anchore_error_json':jsondata})
        raise e

    return(ret)


def anchy_delete(url, raw=False, **kwargs):
    ret = True

    (httpcode, jsondata, rawdata) = fdelete(url, **kwargs)
    if httpcode == 200:
        if raw:
            ret = rawdata
        else:
            if jsondata != None:
                ret = jsondata
            elif rawdata:
                ret = rawdata
            else:
                ret = True
    else:
        e = Exception("failed delete url="+str(url))
        e.__dict__.update({'httpcode':httpcode, 'anchore_error_raw':str(rawdata), 'anchore_error_json':jsondata})
        raise e

    return(ret)
