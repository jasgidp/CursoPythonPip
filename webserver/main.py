import store
from fastapi import FastAPI

from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3]


@app.get('/main', response_class=HTMLResponse)
def get_list():
    return """
<h1>hola sony una pagina</h1>

"""



def run():
    store.getcategories()


if __name__ == '__main__':
    run()