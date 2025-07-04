from mongo_client import db
from bson.objectid import ObjectId
from .utils import get_next_sequence

personas = db['Persona']

def obtener_todos():
    return list(personas.find())

def obtener_por_id(id):
    return personas.find_one({'_id': ObjectId(id)})

def crear(data):
    if 'Tipo_Persona' not in data:
        raise ValueError("El campo Tipo_Persona es obligatorio")
    data['ID_Persona'] = get_next_sequence('persona_id')
    return personas.insert_one(data)

def actualizar(id, data):
    return personas.update_one({'_id': ObjectId(id)}, {'$set': data})

def eliminar(id):
    return personas.delete_one({'_id': ObjectId(id)})

def obtener_por_id_persona(id_persona):
    return personas.find_one({'ID_Persona': id_persona})