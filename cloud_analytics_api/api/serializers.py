from rest_framework import serializers
from cloud_analytics_api.models import (
    ApiCloudDash000001,
    ApiCloudDash000002,
    ApiCloudDash000003,
    # ApiCloudDash000005,
    ApiCloudDash000004,
    ApiCloudDash000005,
    ApiCloudDash000006,
    ApiCloudDash000007,
    ApiCloudDash000008,
    ApiCloudDash000009,
    ApiCloudDash000010,
    ApiCloudDash000011,
    ApiCloudDash000012,
)


class DailySalesRankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000001
        fields = ['vendedor',
                  'vlrvda',
                  'custovda',
                  'vlrdev',
                  'custodev',
                  'vdaliq',
                  'custoliq',
                  'margem',
                  'direto',
                  'lucro',
                  'perclucro'
                  ]


class SalesRankingRegionSerealizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000002
        fields = ['regiao',
                  'vlrvda',
                  'custovda',
                  'vlrdev',
                  'vdaliq',
                  'custoliq',
                  ]


class PreviousDayRankingSerealizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000003
        fields = ['vendedor',
                  'vlrvda',
                  'custovda',
                  'vlrdev',
                  'custodev',
                  'vdaliq',
                  'custoliq',
                  'margem',
                  'direto',
                  'lucro',
                  'perclucro'
                  ]


class SalesAmountDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000004
        fields = ['id',
                  'vlrvda',
                  'custovda',
                  'lucro',
                  'vlrdev',
                  'custodev',
                  'vdaliq',
                  'ppdev',
                  'custoliq',
                  ]


class RepresentativesDailyRankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000005
        fields = ['vendedor',
                  'vlrvda'
                  ]


class SalesAmountLastDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000006
        fields = ['id',
                  'ldvlrvda',
                  'ldcustovda',
                  'ldlucro',
                  'ldvlrdev',
                  'ldcustodev',
                  'ldvdaliq',
                  'ldppdev',
                  'ldcustoliq',
                  ]


# Serializer Purchasing Department
class InventoryValueDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000007
        fields = [
            'DEPARTAMENTO',
            'ESTOQUE_VALOR',
        ]


class SkuNewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000008
        fields = [
            'MES',
            'SKU',
        ]


class StockWithoutTurnoverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000009
        fields = [
            'MARCA',
            'CUSTO_ESTOQUE',
        ]


class MonthlySalesLossSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000010
        fields = [
            'MES',
            'PERDA_VDA_ANO_ATUAL',
            'PERDA_VDA_ANO_ANTERIOR',
        ]


class MonthlyPurchasesWithoutMDFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000011
        fields = [
            'MES',
            'COMPRAS_ANO_ATUAL',
            'COMPRAS_ANO_ANTERIOR',
        ]


class MonthlyPurchasesMDFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCloudDash000012
        fields = [
            'MES',
            'COMPRAS_ANO_ATUAL',
            'COMPRAS_ANO_ANTERIOR',
        ]
