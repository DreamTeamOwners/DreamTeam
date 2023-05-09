from rest_framework import serializers

from apps.resume.models import Resume, Language


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ('name',
                  'surname',
                  'photo',
                  'phone',
                  'position',
                  'description'
                  )


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class MyResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ('id', 'position', 'name', 'surname', 'photo')
