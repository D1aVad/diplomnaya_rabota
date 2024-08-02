from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Создаем экземпляр FastAPI приложения
app = FastAPI()

# Настраиваем шаблонизатор с использованием библиотеки Jinja2
templates = Jinja2Templates(directory='templates')
# Создаем функцию для рендеринга шаблона
@app.get('/')
async def index(request: Request) -> HTMLResponse:
    # Рендерим шаблон 'index.html' и возвращаем результат
    return templates.TemplateResponse('index2.html', {'request': request})

@app.get('/contacts')
async def contacts(request: Request) -> HTMLResponse:
    # Рендерим шаблон 'index.html' и возвращаем результат
    return templates.TemplateResponse('contacts.html', {'request': request})


@app.get('/doppage')
async def dop(request: Request) -> HTMLResponse:
    # Рендерим шаблон 'index.html' и возвращаем результат
    return templates.TemplateResponse('dop_page.html', {'request': request})

    