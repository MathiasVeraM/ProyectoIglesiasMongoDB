from mongo_client import db
from bson.objectid import ObjectId
from .utils import get_next_sequence

sacramentos = db['Sacramento']

def obtener_todos():
    return list(sacramentos.find())

def obtener_por_id(id):
    return sacramentos.find_one({'_id': ObjectId(id)})

def crear(data):
    data['ID_Sacramento'] = get_next_sequence('sacramento_id')
    return sacramentos.insert_one(data)

def actualizar(id, data):
    return sacramentos.update_one({'_id': ObjectId(id)}, {'$set': data})

def eliminar(id):
    return sacramentos.delete_one({'_id': ObjectId(id)})