# Generated by Django 3.2.9 on 2022-06-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accord',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels'),
        ),
        migrations.AlterField(
            model_name='accordoperation',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels'),
        ),
        migrations.AlterField(
            model_name='avenant',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels'),
        ),
        migrations.AlterField(
            model_name='avisjuridique',
            name='avis_pdf',
            field=models.FileField(upload_to='Documents/Avis_juridiques'),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='contrat_pdf',
            field=models.FileField(upload_to='Documents/Contrats'),
        ),
        migrations.AlterField(
            model_name='conventiondedetachement',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels'),
        ),
        migrations.AlterField(
            model_name='historicalsoittransmis',
            name='id_document',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='lettreaccord',
            name='doc_pdf',
            field=models.FileField(upload_to='Documents/Documents_contractuels'),
        ),
        migrations.AlterField(
            model_name='pointdesituation',
            name='pds_pdf',
            field=models.FileField(upload_to='Documents/Point_de_situations'),
        ),
        migrations.AlterField(
            model_name='soittransmis',
            name='id_document',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='soittransmis',
            name='st_pdf',
            field=models.FileField(upload_to='Documents/Soit_transmis'),
        ),
    ]