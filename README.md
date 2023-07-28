# DjangoCrud
Crud en Django para registro control de peso con expotación a CSV y Excel

![vista](https://github.com/BrgarciaG/DjangoCrud/assets/117834766/56a989e1-c0d2-43e4-8788-613d4cc1061c)

* Para instalar se debe ejecutar pip install -r requirements.py
* Se debe congurar la Base de datos (por defecto Postgre usando psycopg2 ) en Archivo .env
* para cargar el modelo a la base de datos se debe ejecutar $python manage.py makemigrations $python manage.py migrate
* se puede cargar un archivo csv ingresando la ruta en importar_csv.py y luego acceder a /registrar desde el nevagador, los campos requeridos son nombre,peso,talla
* sólo se deben registrar los campos indicados anteriormente ya que la aplicacínn calcula el imc y el estado por registro


