from fastapi import FastAPI
from pydantic import BaseModel
import json
from vendas import Vendas

vendas = Vendas()
appVendas = FastAPI()

class Venda(BaseModel):
    id: int
    description: str
    paymentType: int
    value: float

@appVendas.get('/')
def index():
    return {'message': 'Hello World'}

@appVendas.get('/vendas')
def getVendas():
    return vendas.get()

@appVendas.get('/vendas/{venda_id}')
def getById(venda_id):
    return vendas.getOne(int(venda_id))

@appVendas.post('/vendas')
def postVendas(item : Venda):
    description = item.description
    paymentType = item.paymentType
    value = item.value
    return vendas.post(description, paymentType, value)

@appVendas.put('/vendas/')
def putVendas(item : Venda):
    id = item.id
    description = item.description
    paymentType = item.paymentType
    value = item.value
    return vendas.put(int(id), description, paymentType, value)

@appVendas.delete('/vendas/{venda_id}')
def deleteVendas(venda_id):
    return vendas.delete(int(venda_id))

