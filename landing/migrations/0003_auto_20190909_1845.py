# Generated by Django 2.2.5 on 2019-09-09 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20190909_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='prof_favorito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='professor.Professor'),
        ),
    ]