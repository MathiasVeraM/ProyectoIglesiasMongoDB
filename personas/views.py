from django.shortcuts import render, redirect
from .services import persona_services
from parroquias.services import parroquia_services
import json

def listar_personas(request):
    personas = persona_services.obtener_todos()
    for p in personas:
        p['id_str'] = str(p['_id'])
    return render(request, 'personas/lista.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        tipo = request.POST['Tipo_Persona']
        data = {
            'Nombre_Persona': request.POST['Nombre_Persona'],
            'Apellido_Persona': request.POST['Apellido_Persona'],
            'Telefono_Persona': request.POST['Telefono_Persona'],
            'Email_Persona': request.POST['Email_Persona'],
            'Tipo_Persona': tipo
        }

        # Subdocumento según tipo
        if tipo == 'Catequizado':
            data['Catequizado'] = {
                'Fecha_Nacimiento_Catequizado': request.POST['Fecha_Nacimiento_Catequizado'],
                'Sexo_Catequizado': request.POST['Sexo_Catequizado'],
                'Direccion_Catequizado': request.POST['Direccion_Catequizado'],
                'Catequizado_Bautizado': 'Catequizado_Bautizado' in request.POST,
                'ID_Parroquia': int(request.POST['ID_Parroquia']),
                'ID_Representante': int(request.POST['ID_Representante'])
            }
        elif tipo == 'Catequista':
            data['Catequista'] = {
                'ID_Parroquia': int(request.POST['ID_Parroquia'])
            }
        elif tipo == 'Representante':
            data['Representante'] = {}  # Solo el ID se generará

        persona_services.crear(data)
        return redirect('/personas/')

    parroquias = list(parroquia_services.obtener_todas())
    representantes = [r for r in persona_services.obtener_todos() if r['Tipo_Persona'] == 'Representante']

    return render(request, 'personas/formulario.html', {
    'parroquias': json.dumps(parroquias, default=str),
    'representantes': json.dumps(representantes, default=str)
})

def editar_persona(request, id):
    persona = persona_services.obtener_por_id(id)
    if request.method == 'POST':
        tipo = request.POST['Tipo_Persona']
        data = {
            'Nombre_Persona': request.POST['Nombre_Persona'],
            'Apellido_Persona': request.POST['Apellido_Persona'],
            'Telefono_Persona': request.POST['Telefono_Persona'],
            'Email_Persona': request.POST['Email_Persona'],
            'Tipo_Persona': tipo
        }

        # Subdocumento según tipo
        if tipo == 'Catequizado':
            data['Catequizado'] = {
                'Fecha_Nacimiento_Catequizado': request.POST['Fecha_Nacimiento_Catequizado'],
                'Sexo_Catequizado': request.POST['Sexo_Catequizado'],
                'Direccion_Catequizado': request.POST['Direccion_Catequizado'],
                'Catequizado_Bautizado': 'Catequizado_Bautizado' in request.POST,
                'ID_Parroquia': int(request.POST['ID_Parroquia']),
                'ID_Representante': int(request.POST['ID_Representante'])
            }
        elif tipo == 'Catequista':
            data['Catequista'] = {
                'ID_Parroquia': int(request.POST['ID_Parroquia'])
            }
        elif tipo == 'Representante':
            data['Representante'] = {}

        persona_services.actualizar(id, data)
        return redirect('/personas/')
    return render(request, 'personas/formulario.html', {'persona': persona})

def eliminar_persona(request, id):
    persona_services.eliminar(id)
    return redirect('/personas/')

def detalle_persona(request, id):
    persona = persona_services.obtener_por_id(id)
    persona['id_str'] = str(persona['_id'])  # por si se necesita en el template
    return render(request, 'personas/detalle.html', {'persona': persona})