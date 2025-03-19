from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola, mundo! Esta es mi primera página en Django.")
