from django.template import loader
from django.http import HttpResponse

def index(request):
    diccionario = {"nombre":"Coder"}
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(diccionario)
    return HttpResponse("")