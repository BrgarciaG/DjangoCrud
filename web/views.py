from django.shortcuts import render,redirect
from .importar_csv import ObtieneRegistros
from .models import Persona
from .formulas import Formulas
import csv
from django.http import HttpResponse
import xlsxwriter


# la siguiente vista (home) tiene por objetivo cargar los registros desde un archivo csv, se debe modifica la ruta en importar_csv.py
# el formato es nombre,peso,talla
# Formulas.imc se encarga de calcular el imc, luego la vista registra todos los datos en el modelo Persona
def home(request):
    listado = len(ObtieneRegistros.leer())
    for registro in ObtieneRegistros.leer():
        imc = Formulas.imc(registro[1],registro[2])
        Persona.objects.create(nombre= registro[0],peso=registro[1],talla=registro[2],imc=imc[0],estado=imc[1])
        print(f"Se registro: {registro[0]}")
    return render(request,'registro.html',{'listado':listado,'registros': ObtieneRegistros.leer()})

def listado(request):
    if request.method =='POST':
        nombre = request.POST['nombre']
        peso = request.POST['peso']
        talla = request.POST['talla']
        imc = Formulas.imc(peso,talla)
        Persona.objects.create(nombre=nombre,peso=peso,talla=talla,imc=imc[0],estado=imc[1])
        return redirect('/')
    else:
        listado = Persona.objects.all().order_by('-id').values()
        return render(request,'listado.html',{'listado':listado})

def modifica(request):
    if request.method =='POST':
        ide = request.POST['idForm']
        nombre = request.POST['nombreForm']
        peso = request.POST['pesoForm']
        talla = request.POST['tallaForm']
        imc = Formulas.imc(peso,talla)
        Persona.objects.filter(id=ide).update(nombre=nombre,peso=peso,talla=talla,imc=imc[0],estado=imc[1])
        return redirect('/')
    else:
        return redirect('/')

def elimina(request,ide):
    Persona.objects.get(id=ide).delete()
    return redirect('/')

def exportaCSV(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="listado.csv"'},
    )
    registros = Persona.objects.all()
    writer = csv.writer(response,delimiter=';')
    writer.writerow(['nombre','peso','talla','imc','estado'])
    for registro in registros:
        writer.writerow([registro.nombre,registro.peso,registro.talla,registro.imc,registro.estado])

    return response

def exportaExcel(request):
    response = HttpResponse(
        content_type='application/vnd.ms-excel',
        headers={'Content-Disposition': 'attachment; filename="listado.xlsx"'},
    )
    registros = Persona.objects.all()
    
    workbook = xlsxwriter.Workbook(response)
    sheet = workbook.add_worksheet('Pacientes')

    sheet.write('A1', 'Nombre')
    sheet.write('B1', 'Peso(g)')
    sheet.write('C1', 'Talla(cm)')
    sheet.write('D1', 'Imc')
    sheet.write('E1', 'Estado')
    fila=1
    for registro in registros:
        fila = fila + 1
        sheet.write(f'A{fila}', registro.nombre)
        sheet.write(f'B{fila}', registro.peso)
        sheet.write(f'C{fila}', registro.talla)
        sheet.write(f'D{fila}', registro.imc)
        sheet.write(f'E{fila}', registro.estado)

    workbook.close()
       
    return response