from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Admin(models.Model):
    cedula_admin = models.CharField(max_length=11, primary_key=True)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)

    class Meta:
        ordering = ('-cedula_admin',)

    def __str__(self):
        return self.cedula_admin


class Categoria(models.Model):
    id_categoria = models.CharField(max_length=200, primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)

    class Meta:
        ordering = ('-especie',)

    def __str__(self):
        return self.especie


class Producto(models.Model):
    id_producto = models.CharField(max_length=200, primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    precio_producto = models.IntegerField()
    precio_produccion = models.IntegerField()
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    especificaciones = models.CharField(max_length=1000, default=None)
    admin_producto = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-precio_producto', '-nombre_producto')

    def __str__(self):
        return self.nombre_producto


class Cliente(models.Model):
    id_cliente = models.CharField(max_length=200, primary_key=True)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)

    class Meta:
        ordering = ('-nombre1', '-apellido1')

    def __str__(self):
        return self.id_cliente



class Carrito(models.Model):
    id_carrito = models.CharField(max_length=200, primary_key=True)
    id_producto = models.CharField(max_length=200)
    cantidad_producto = models.SmallIntegerField()
    total_producto = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id_carrito', '-id_producto')

    def __str__(self):
        return self.id_carrito




class Cuenta(models.Model):
    numero_cuenta = models.CharField(max_length=200, primary_key=True)
    valor_total = models.IntegerField()
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)


    class Meta:
        ordering = ('-numero_cuenta', '-valor_total')

    def __str__(self):
        return self.id_carrito


class Domiciliario(models.Model):
    id_domiciliario = models.CharField(max_length=200, primary_key=True)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    medio_transporte = models.CharField(max_length=50)

    class Meta:
        ordering = ('-id_domiciliario', '-medio_transporte')

    def __str__(self):
        return self.id_domiciliario


class Domicilio(models.Model):
    id_domicilio = models.CharField(max_length=200, primary_key=True)
    id_domiciliario = models.ForeignKey(Domiciliario,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    numero_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE)
    metodo_de_pago = models.CharField(max_length=50)

    class Meta:
        ordering=('-id_domicilio','-id_domiciliario')

    def __str__(self):
        return self.id_domicilio




