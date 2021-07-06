from rest_framework.viewsets import ModelViewSet
from backend.serializers import LanguageSerializer, CourseSerializer, VocabularySerializer, SensesSerializer, ExerciseSerializer
from backend.models import Language, Course, Vocabulary, Senses, Exercise
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend, BaseInFilter, NumberFilter


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.order_by('pk')
    serializer_class = LanguageSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['name', ]


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.order_by('pk')
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['name', ]


class VocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.order_by('pk')
    serializer_class = VocabularySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['course', ]


class SensesViewSet(ModelViewSet):
    queryset = Senses.objects.order_by('pk')
    serializer_class = SensesSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['course','accent', ]


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.order_by('pk')
    serializer_class = ExerciseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['course','accent', ]
