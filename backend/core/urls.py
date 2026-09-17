from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from attendance.views import ClockInAPIView, ClockOutAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Employee Authentication
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Mobile Time Tracking
    path('api/attendance/clock-in/', ClockInAPIView.as_view(), name='clock_in'),
    path('api/attendance/clock-out/', ClockOutAPIView.as_view(), name='clock_out'),
]