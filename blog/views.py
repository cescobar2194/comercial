from django.shortcuts import render, get_object_or_404,redirect
from django.utils  import timezone
from .models import Publicacion
from .forms import PubForm

def listar_pub(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})

def detalle_pub(request,pk):
    p = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_pub.html', {'p':p})

def nueva_pub(request):
    if request.method == "POST":
        f = PubForm(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.autor = request.user
            p.save()
            return redirect('detalle_pub', pk=p.pk)
    else:
        f = PubForm()
    return render(request, 'blog/editar_pub.html', {'f': f})

def editar_pub(request, pk):
    p = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        f = PubForm(request.POST, instance=p)
        if f.is_valid():
            p = form.save(commit=False)
            p.autor = request.user
            p.save()
            return redirect('detalle_pub', pk=p.pk)
    else:
        f = PubForm(instance=p)
    return render(request, 'blog/editar_pub.html', {'f': f})

def lista_borradores(request):
    pubs = Publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/lista_borradores.html', {'pubs': pubs})

def publicar_publicacion(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.publicar()
    return redirect('detalle_pub', pk=pk)

def eliminar_publicacion(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    post.delete()
    return redirect('listar_pub')
