# Generated by Django 3.0.4 on 2020-03-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9)),
                ('cidade', models.CharField(default='Cândido Sales', max_length=100)),
                ('cidade_id', models.TextField()),
                ('estado', models.CharField(default='Bahia', max_length=50)),
                ('estado_id', models.TextField()),
            ],
        ),
    ]
