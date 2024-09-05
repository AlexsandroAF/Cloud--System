from django.db import models


# Finance API
class ApiCloudDash000001(models.Model):
    vendedor = models.CharField(max_length=80, db_collation='USING_NLS_COMP', blank=True, primary_key=True,
                                unique=False)
    vlrvda = models.FloatField(blank=True, null=True)
    custovda = models.FloatField(blank=True, null=True)
    vlrdev = models.FloatField(blank=True, null=True)
    custodev = models.FloatField(blank=True, null=True)
    vdaliq = models.FloatField(blank=True, null=True)
    custoliq = models.FloatField(blank=True, null=True)
    margem = models.FloatField(blank=True, null=True)
    direto = models.FloatField(blank=True, null=True)
    lucro = models.FloatField(blank=True, null=True)
    perclucro = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.vendedor

    class Meta:
        verbose_name_plural = "Ranking De Vendedores"
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000001'
        ordering = ['-vlrvda']


class ApiCloudDash000002(models.Model):
    regiao = models.CharField(max_length=40, db_collation='USING_NLS_COMP', blank=True, primary_key=True, unique=False)
    vlrvda = models.FloatField(blank=True, null=True)
    custovda = models.FloatField(blank=True, null=True)
    vlrdev = models.FloatField(blank=True, null=True)
    custodev = models.FloatField(blank=True, null=True)
    vdaliq = models.FloatField(blank=True, null=True)
    custoliq = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.regiao

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000002'
        ordering = ['regiao']


class ApiCloudDash000003(models.Model):
    vendedor = models.CharField(max_length=121, db_collation='USING_NLS_COMP', blank=True, primary_key=True,
                                unique=False)
    vlrvda = models.FloatField(blank=True, null=True)
    custovda = models.FloatField(blank=True, null=True)
    vlrdev = models.FloatField(blank=True, null=True)
    custodev = models.FloatField(blank=True, null=True)
    vdaliq = models.FloatField(blank=True, null=True)
    custoliq = models.FloatField(blank=True, null=True)
    margem = models.FloatField(blank=True, null=True)
    direto = models.FloatField(blank=True, null=True)
    lucro = models.FloatField(blank=True, null=True)
    perclucro = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.vendedor

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000003'


class ApiCloudDash000004(models.Model):
    id = models.CharField(max_length=115, primary_key=True, unique=False)
    vlrvda = models.FloatField(blank=True, null=True)
    custovda = models.FloatField(blank=True, null=True)
    lucro = models.FloatField(blank=True, null=True)
    vlrdev = models.FloatField(blank=True, null=True)
    custodev = models.FloatField(blank=True, null=True)
    vdaliq = models.FloatField(blank=True, null=True)
    ppdev = models.FloatField(blank=True, null=True)
    custoliq = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.vlrvda

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000004'


class ApiCloudDash000005(models.Model):
    vendedor = models.CharField(max_length=80, db_collation='USING_NLS_COMP', blank=True, primary_key=True,
                                unique=False)
    vlrvda = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.vendedor

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000005'
        ordering = ['vendedor']


class ApiCloudDash000006(models.Model):
    id = models.CharField(max_length=115, primary_key=True, unique=False)
    ldvlrvda = models.FloatField(blank=True, null=True)
    ldcustovda = models.FloatField(blank=True, null=True)
    ldlucro = models.FloatField(blank=True, null=True)
    ldvlrdev = models.FloatField(blank=True, null=True)
    ldcustodev = models.FloatField(blank=True, null=True)
    ldvdaliq = models.FloatField(blank=True, null=True)
    ldppdev = models.FloatField(blank=True, null=True)
    ldcustoliq = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.ldvlrvda

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000006'


""" 
Compras API 
"""


# Valor Em Estoque Por Departamento
class ApiCloudDash000007(models.Model):
    DEPARTAMENTO = models.CharField(max_length=115, primary_key=True, unique=False)
    ESTOQUE_VALOR = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.DEPARTAMENTO

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000007'


# SKUS Novos
class ApiCloudDash000008(models.Model):
    MES = models.CharField(max_length=115, primary_key=True, unique=False)
    SKU = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.MES

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000008'


# Ranking De Estoque Sem Giro Separado Por Marca
class ApiCloudDash000009(models.Model):
    MARCA = models.CharField(max_length=115, primary_key=True, unique=False)
    CUSTO_ESTOQUE = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.MARCA

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000009'


# Perca de Venda Mensal
class ApiCloudDash000010(models.Model):
    MES = models.CharField(max_length=115, primary_key=True, unique=False)
    PERDA_VDA_ANO_ATUAL = models.FloatField(blank=True, null=True)
    PERDA_VDA_ANO_ANTERIOR = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.MES

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000010'


# Grafico de Compras Mensal - Sem MDF Bianual
class ApiCloudDash000011(models.Model):
    MES = models.CharField(max_length=115, primary_key=True, unique=False)
    COMPRAS_ANO_ATUAL = models.FloatField(blank=True, null=True)
    COMPRAS_ANO_ANTERIOR = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.MES

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000011'


# Grafico de Compras Mensal - MDF Bianual
class ApiCloudDash000012(models.Model):
    MES = models.CharField(max_length=115, primary_key=True, unique=False)
    COMPRAS_ANO_ATUAL = models.FloatField(blank=True, null=True)
    COMPRAS_ANO_ANTERIOR = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.MES

    class Meta:
        app_label = 'cloud_analytics_api'
        managed = False  # Created from a view. Don't remove.
        db_table = 'api_cloud_dash_000012'
