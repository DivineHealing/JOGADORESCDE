# Generated by Django 5.1.6 on 2025-05-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tela_personagem', '0002_rename_vidabasecalc_tela_personagem_vidafixabase_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tela_personagem',
            name='vidaFinal',
            field=models.IntegerField(blank=True, default=100),
        ),
    ]
