from rest_framework.viewsets import ModelViewSet
from measurements.models import Project, Measurement
from measurements.serializers import MeasurementSerializer, ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
