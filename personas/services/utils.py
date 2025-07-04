from mongo_client import db

def get_next_sequence(nombre_secuencia):
    counters = db['counters']
    secuencia = counters.find_one_and_update(
        {'_id': nombre_secuencia},
        {'$inc': {'valor': 1}},
        upsert=True,
        return_document=True
    )
    return secuencia['valor']