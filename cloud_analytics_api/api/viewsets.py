from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from cloud_analytics_api.api.serializers import (
    DailySalesRankingSerializer,
    SalesRankingRegionSerealizer,
    PreviousDayRankingSerealizer,
    RepresentativesDailyRankingSerializer,
    SalesAmountDaySerializer,
    SalesAmountLastDaySerializer,
    InventoryValueDepartmentSerializer,
    SkuNewSerializer,
    StockWithoutTurnoverSerializer,
    MonthlySalesLossSerializer,
    MonthlyPurchasesWithoutMDFSerializer,
    MonthlyPurchasesMDFSerializer,
)

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

"""
API endpoint that allows users to be viewed or edited.
"""


# ViewSet Finance

class DailySalesRankingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000001.objects.all()[:5]
    serializer_class = DailySalesRankingSerializer


class RankingRegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000002.objects.all()
    serializer_class = SalesRankingRegionSerealizer


class PreviousDayRankingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000003.objects.all()
    serializer_class = PreviousDayRankingSerealizer


class SalesAmountDayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000004.objects.all()
    serializer_class = SalesAmountDaySerializer


class RepresentativesDailyRankingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000005.objects.all()
    serializer_class = RepresentativesDailyRankingSerializer


class SalesAmountLastDayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000006.objects.all()
    serializer_class = SalesAmountLastDaySerializer


# ViewSet Purchasing Department
class InventoryValueDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000007.objects.all()
    serializer_class = InventoryValueDepartmentSerializer


class SkuNewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000008.objects.all()
    serializer_class = SkuNewSerializer


class StockWithoutTurnoverViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000009.objects.all()
    serializer_class = StockWithoutTurnoverSerializer


class MonthlySalesLossViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000010.objects.all()
    serializer_class = MonthlySalesLossSerializer


class MonthlyPurchasesWithoutMDFViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000011.objects.all()
    serializer_class = MonthlyPurchasesWithoutMDFSerializer


class MonthlyPurchasesMDFViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApiCloudDash000012.objects.all()
    serializer_class = MonthlyPurchasesMDFSerializer
