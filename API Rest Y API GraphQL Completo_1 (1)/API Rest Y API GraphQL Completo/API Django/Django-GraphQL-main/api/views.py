from django.shortcuts import render, redirect
from django.shortcuts import render

def post_form(request):
    from .models import Publicacion, Category

    categories = Category.objects.all()

    if request.method == 'POST':
        print("POST recibido")
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        categoria_id = request.POST.get('categoria')

        print(f"titulo: {titulo}, contenido: {contenido}, categoria_id: {categoria_id}")

        if titulo and contenido and categoria_id:
            categoria = Category.objects.get(id=categoria_id)
            print(f"Categoria: {categoria}")
            Publicacion.objects.create(titulo=titulo, contenido=contenido, categoria=categoria)
            print("Publicacion creada")
            return redirect(request.path)  # recarga la misma página
        else:
            print("Faltan datos en el formulario")

    return render(request, 'post_form.html', {'categories': categories})

def publicaciones(request):
    return render(request, 'publicaciones.html')

