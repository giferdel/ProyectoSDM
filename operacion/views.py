from django.shortcuts import render


def mi_vista(request):
    contexto = {
        'mensaje': 'Este es un mensaje desde la vista.',
        'cantidad': '18'
    }
    return render(request, 'index.html', contexto)