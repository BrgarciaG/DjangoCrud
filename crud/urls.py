
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/', views.home, name="registro"),# ruta definida para efectuar la carga de un archivo csv, ver función home en views
    path('', views.listado, name="listado"),
    path('modifica/', views.modifica, name="editar"),
    path('elimina/<int:ide>', views.elimina,name="elimina"),
    path('exportaCSV/', views.exportaCSV, name="exportaCSV"),
    path('exportaExcel/', views.exportaExcel, name="exportaExcel"),    
]
