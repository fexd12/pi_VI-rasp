import requests

def cadastrar(tag):
    payload = {
        'tag' : tag
    }
    try:

        requests.post('http://localhost:2000/tag/',payload)
        
    except Exception as e :
        raise

    # realizar cadsatro tag
