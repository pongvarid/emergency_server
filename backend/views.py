from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.serializers import *
from backend.models import Course, Vocabulary, Accent, Senses, Exercise


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.order_by('pk')
    serializer_class = CourseSerializer



class VocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.order_by('pk')
    serializer_class = VocabularySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['course', 'accent']


class AccentViewSet(ModelViewSet):
    queryset = Accent.objects.order_by('pk')
    serializer_class = AccentSerializer


class SensesViewSet(ModelViewSet):
    queryset = Senses.objects.order_by('pk')
    serializer_class = SensesSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['course', 'accent']


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.order_by('pk')
    serializer_class = ExerciseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['course', 'accent']




