from rest_framework.serializers import ModelSerializer
from backend.models import Language, Course, Vocabulary, Senses, Exercise


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class VocabularySerializer(ModelSerializer):

    class Meta:
        model = Vocabulary
        fields = '__all__'


class SensesSerializer(ModelSerializer):

    class Meta:
        model = Senses
        fields = '__all__'


class ExerciseSerializer(ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'
