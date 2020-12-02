# Generated by Django 3.1.3 on 2020-12-01 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cédula', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=100)),
                ('dirección', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-primer_nombre', '-primer_apellido'),
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductoCarrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito_compra.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.BooleanField(default=False)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_pedido', models.DateTimeField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito_compra.cliente')),
                ('items', models.ManyToManyField(to='carrito_compra.ProductoCarrito')),
            ],
        ),
    ]
