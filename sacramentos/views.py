from django.shortcuts import render, redirect
from .services import sacramento_services

def listar_sacramentos(request):
    sacramentos = sacramento_services.obtener_todos()
    for s in sacramentos:
        s['id_str'] = str(s['_id'])
    return render(request, 'sacramentos/lista.html', {'sacramentos': sacramentos})

def crear_sacramento(request):
    if request.method == 'POST':
        data = {
            'Nombre_Sacramento': request.POST['Nombre_Sacramento'],
            'Sacramento_Requiere_Padrino': 'Sacramento_Requiere_Padrino' in request.POST
        }
        sacramento_services.crear(data)
        return redirect('/sacramentos/')
    return render(request, 'sacramentos/formulario.html', {'sacramento': None})

def editar_sacramento(request, id):
    sacramento = sacramento_services.obtener_por_id(id)
    if request.method == 'POST':
        data = {
    'Nombre_Sacramento': request.POST['Nombre_Sacramento'],
    'Sacramento_Requiere_Padrino': 'Sacramento_Requiere_Padrino' in request.POST
}
        sacramento_services.actualizar(id, data)
        return redirect('/sacramentos/')
    return render(request, 'sacramentos/formulario.html', {'sacramento': sacramento})

def eliminar_sacramento(request, id):
    sacramento_services.eliminar(id)
    return redirect('/sacramentos/')
