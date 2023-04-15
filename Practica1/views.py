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
    periodo=agno-2023 # Estamos en 2023
    edadfutura=edad+periodo

    '''
    Esta línea en Python es una cadena de texto que contiene etiquetas HTML y una cadena de formato (%s) que se usa para incrustar variables dentro de la cadena.
    En este caso, la cadena de formato espera dos variables: "agno" y "edadfutura".
    La sintaxis "%(agno, edadfutura)" al final de la cadena se utiliza para proporcionar los valores de las variables que se deben incrustar en la cadena de formato.
    '''
    documento="<html><body><h2>En el año %s tendras %s años " %(agno,edadfutura)
    
    return HttpResponse(documento)
    