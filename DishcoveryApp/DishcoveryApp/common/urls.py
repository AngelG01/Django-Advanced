from django.urls import path

from DishcoveryApp.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
]
