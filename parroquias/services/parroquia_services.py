from mongo_client import db
from bson.objectid import ObjectId
from .utils import get_next_sequence

parroquias = db['Parroquia']

def obtener_todas():
    return list(parroquias.find())

def obtener_por_id(id_parroquia):
    return db['Parroquia'].find_one({'ID_Parroquia': id_parroquia})

def crear(data):
    data['ID_Parroquia'] = get_next_sequence('parroquia_id')
    return parroquias.insert_one(data)

def actualizar(id, data):
    return parroquias.update_one({'_id': ObjectId(id)}, {'$set': data})

def eliminar(id):
    return parroquias.delete_one({'_id': ObjectId(id)})

