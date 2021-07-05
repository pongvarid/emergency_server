from rest_framework.serializers import ModelSerializer
from backend.models import Course, Vocabulary, Accent, Senses, Exercise


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class VocabularySerializer(ModelSerializer):

    class Meta:
        model = Vocabulary
        fields = '__all__'

    def get_named(self, obj):
        try:
            course = Course.objects.get(id=obj.course_id)
            accent = Accent.objects.get(id=obj.accent_id)
            return course.name, accent.name
        except:
            return None


class AccentSerializer(ModelSerializer):

    class Meta:
        model = Accent
        fields = '__all__'


class SensesSerializer(ModelSerializer):

    class Meta:
        model = Senses
        fields = '__all__'

    def get_named(self,obj):
        try:
            course = Course.objects.get(id=obj.course_id)
            accent = Accent.objects.get(id=obj.accent_id)
            return course.name, accent.name
        except:
            return None


class ExerciseSerializer(ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'

    def get_named(self, obj):
        try:
            course = Course.objects.get(id=obj.course_id)
            accent = Accent.objects.get(id=obj.accent_id)
            return course.name, accent.name
        except:
            return None


