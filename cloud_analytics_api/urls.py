from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework import routers

from cloud_analytics_api.api.viewsets import (
    # ViewSet Finance API
    DailySalesRankingViewSet,
    RankingRegionViewSet,
    PreviousDayRankingViewSet,
    RepresentativesDailyRankingViewSet,
    SalesAmountDayViewSet,
    SalesAmountLastDayViewSet,
    # ViewSet  Purchasing Department API
    InventoryValueDepartmentViewSet,
    SkuNewViewSet,
    StockWithoutTurnoverViewSet,
    MonthlySalesLossViewSet,
    MonthlyPurchasesWithoutMDFViewSet,
    MonthlyPurchasesMDFViewSet,

    )

router = routers.DefaultRouter()
# Router Finance API
router.register(r'ranking-sales', DailySalesRankingViewSet)
router.register(r'ranking-region', RankingRegionViewSet)
router.register(r'ranking-sales-previous-day', PreviousDayRankingViewSet)
router.register(r'representative-daily-ranking', RepresentativesDailyRankingViewSet)
router.register(r'sales-amount-day', SalesAmountDayViewSet)
router.register(r'sales-amount-last-day', SalesAmountLastDayViewSet)

# Router Purchasing Department API
router.register(r'inventory-value-department', InventoryValueDepartmentViewSet)
router.register(r'sku-new', SkuNewViewSet)
router.register(r'stock-without-turnover', StockWithoutTurnoverViewSet)
router.register(r'monthly-sales-loss', MonthlySalesLossViewSet)
router.register(r'monthly-purchases-without-mdf', MonthlyPurchasesWithoutMDFViewSet)
router.register(r'monthly-purchases-mdf', MonthlyPurchasesMDFViewSet)

#

# URL
urlpatterns = [
    # API
    path('analytic/api/', include(router.urls)),
]
