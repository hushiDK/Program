import requests



# hihh='http://httpbin.org/get'
def api(x):

    # r = requests.get('http://httpbin.org/get')
    r = requests.get(x)
    return (r.status_code)


# y=api(hihh)
