from django.db import models
class Cliente(models.Model):
    nombre =models.CharField(max_length=200)
    Tipo_doc =models.CharField(max_length=20)
    telefono =models.CharField(max_length=20)
    correo =models.EmailField(max_length=200)
    direccion =models.CharField(max_length=50)
    cantidad =models.CharField(max_length=45)
    estado =models.BooleanField()

# Modelo





