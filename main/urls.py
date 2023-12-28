from django.urls import path

from main.views import NetworkUnitListAPIView, NetworkUnitDetailAPIView, NetworkUnitCreateAPIView, \
    NetworkUnitUpdateAPIView, NetworkUnitDestroyAPIView, MyTokenObtainPairView

app_name = 'main'

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('networkunits/', NetworkUnitListAPIView.as_view(), name='networkunits_list'),
    path('networkunits/<int:pk>', NetworkUnitDetailAPIView.as_view(), name='networkunit_detail'),
    path('networkunits/create/', NetworkUnitCreateAPIView.as_view(), name='networkunit_create'),
    path('networkunits/update/<int:pk>', NetworkUnitUpdateAPIView.as_view(), name='networkunit_update'),
    path('networkunits/delete/<int:pk>', NetworkUnitDestroyAPIView.as_view(), name='networkunit_delete'),
]
