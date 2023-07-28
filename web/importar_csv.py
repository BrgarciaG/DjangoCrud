import csv

class ObtieneRegistros():
    def leer():
        lista=[]
        with open("ruta a archivo .csv", newline='') as csvfile:
            listado = csv.reader(csvfile, delimiter=';')
            next(listado)
            for row in listado:
                lista.append(row)
        return lista


