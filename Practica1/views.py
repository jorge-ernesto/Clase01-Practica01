from django.http import HttpResponse
import datetime

def saludo(request):
    
    documento="""<html>
    <body>
     <h1>
      Hola alumnos esta es nuestra primera pagina con Django
     </h1>
    </body>
    </html> """
     
    return HttpResponse(documento)

def despedida(request):
    
    return HttpResponse("Hasta luego alumnos de Django")

def damefecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento=f"""<html>
    <body>
     <h1>
      Fecha y Hora actuales  %s
     </h1>
    </body>
    </html> {fecha_actual} """
     
    return HttpResponse(documento)

def calculaedad(request, edad, agno):
    
    #edadactual=18
    periodo=agno-2022
    edadfutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años " %(agno,edadfutura)
    
    return HttpResponse(documento)
    