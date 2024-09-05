# Generated by Django 4.2.5 on 2023-09-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_analytics_api', '0003_apiclouddash000006_alter_apiclouddash000001_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiCloudDash000007',
            fields=[
                ('DEPARTAMENTO', models.CharField(max_length=115, primary_key=True, serialize=False)),
                ('ESTOQUE_VALOR', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'api_cloud_dash_000007',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiCloudDash000008',
            fields=[
                ('MES', models.CharField(max_length=115, primary_key=True, serialize=False)),
                ('SKU', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'api_cloud_dash_000008',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiCloudDash000009',
            fields=[
                ('MARCA', models.CharField(max_length=115, primary_key=True, serialize=False)),
                ('CUSTO_ESTOQUE', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'api_cloud_dash_000009',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiCloudDash000010',
            fields=[
                ('MES', models.CharField(max_length=115, primary_key=True, serialize=False)),
                ('PERDA_VDA_ANO_ATUAL', models.FloatField(blank=True, null=True)),
                ('PERDA_VDA_ANO_ANTERIOR', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'api_cloud_dash_000010',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiCloudDash000011',
            fields=[
                ('MES', models.CharField(max_length=115, primary_key=True, serialize=False)),
                ('COMPRAS_ANO_ATUAL', models.FloatField(blank=True, null=True)),
                ('COMPRAS_ANO_ANTERIOR', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'api_cloud_dash_000011',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApiCloudDash000012',
            fields=[
                ('MES', models.CharField(max_length=115, primary_key=True, serialize=False)),
                ('COMPRAS_ANO_ATUAL', models.FloatField(blank=True, null=True)),
                ('COMPRAS_ANO_ANTERIOR', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'api_cloud_dash_000012',
                'managed': False,
            },
        ),
    ]