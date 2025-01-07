from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - merchant-slabs-coll-d79cbacbd78a4103b70bee3689814092',debug=False,docs_url='/nice-aditya-69e8ee1cccdf11efbacf0242ac12000482/docs',openapi_url='/nice-aditya-69e8ee1cccdf11efbacf0242ac12000482/openapi.json')

app.include_router(router, prefix='/nice-aditya-69e8ee1cccdf11efbacf0242ac12000482/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()