# Generated by Django 5.1.6 on 2025-05-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_personagem', '0002_rename_danofixo_1_base_personagem_dreno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='base_personagem',
            name='mana',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='base_personagem',
            name='vidaBase',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='base_personagem',
            name='vigor',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='base_personagem',
            name='regenMana',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='base_personagem',
            name='regenVida',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='base_personagem',
            name='regenVigor',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
