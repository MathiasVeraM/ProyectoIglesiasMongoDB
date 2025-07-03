from django.shortcuts import render, redirect
from .services import parroquia_services
from bson.objectid import ObjectId

def listar_parroquias(request):
    parroquias = parroquia_services.obtener_todas()
    for p in parroquias:
        p['id_str'] = str(p['_id'])
    return render(request, 'parroquias/lista.html', {'parroquias': parroquias})

def crear_parroquia(request):
    if request.method == 'POST':
        data = {
            'Nombre_Parroquia': request.POST['Nombre_Parroquia'],
            'Direccion_Parroquia': request.POST['Direccion_Parroquia'],
            'Telefono_Parroquia': request.POST['Telefono_Parroquia'],
            'Email_Parroquia': request.POST['Email_Parroquia'],
            'Es_Principal_Parroquia': 'Es_Principal_Parroquia' in request.POST
        }
        parroquia_services.crear(data)
        return redirect('/parroquias/')
    return render(request, 'parroquias/formulario.html', {'parroquia': None})

def editar_parroquia(request, id):
    parroquia = parroquia_services.obtener_por_id(id)
    if request.method == 'POST':
        data = {
            'Nombre_Parroquia': request.POST['Nombre_Parroquia'],
            'Direccion_Parroquia': request.POST['Direccion_Parroquia'],
            'Telefono_Parroquia': request.POST['Telefono_Parroquia'],
            'Email_Parroquia': request.POST['Email_Parroquia'],
            'Es_Principal_Parroquia': 'Es_Principal_Parroquia' in request.POST
        }
        parroquia_services.actualizar(id, data)
        return redirect('/parroquias/')
    return render(request, 'parroquias/formulario.html', {'parroquia': parroquia})

def eliminar_parroquia(request, id):
    parroquia_services.eliminar(id)
    return redirect('/parroquias/')