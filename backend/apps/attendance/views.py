from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.utils import timezone
from .models import AttendanceRecord

class ClockInAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if AttendanceRecord.objects.filter(employee=request.user, clock_out__isnull=True).exists():
            return Response({"error": "You are already clocked in."}, status=status.HTTP_400_BAD_REQUEST)

        record = AttendanceRecord.objects.create(employee=request.user)
        return Response({
            "message": "Clocked in successfully.",
            "id": record.id,
            "clock_in": record.clock_in
        }, status=status.HTTP_201_CREATED)

class ClockOutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        record = AttendanceRecord.objects.filter(employee=request.user, clock_out__isnull=True).first()
        if not record:
            return Response({"error": "No active clock-in record found."}, status=status.HTTP_400_BAD_REQUEST)

        record.clock_out = timezone.now()
        record.save()
        return Response({
            "message": "Clocked out successfully.",
            "clock_out": record.clock_out
        }, status=status.HTTP_200_OK)