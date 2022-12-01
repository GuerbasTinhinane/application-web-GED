# Generated by Django 3.2.9 on 2022-06-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220619_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accord',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels/Accords'),
        ),
        migrations.AlterField(
            model_name='accordoperation',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels/Accords_operations'),
        ),
        migrations.AlterField(
            model_name='avenant',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels/Avenant'),
        ),
        migrations.AlterField(
            model_name='conventiondedetachement',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels/Conventions'),
        ),
        migrations.AlterField(
            model_name='lettreaccord',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels/Lettres_accords'),
        ),
    ]
