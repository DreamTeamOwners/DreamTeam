from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import MyUser, Profile, Message, Group, Comment


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token


class MyUserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = [
            'id',
            'email',
            'username',
            'password',
        ]


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email']


class ProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['first_name', 'job_position',
                 'last_name', 'phone_number', 'country', 'description', 'city', 'github',
                 'experience_start_time', 'experience_end_time', 'experience_title', 'experience_description',
                 'education_end_year', 'education_place', 'education_title', 'image']


class MyProfileSerializer(serializers.ModelSerializer):
    completion_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'job_position', 'first_name', 'last_name', 'phone_number', 'country', 'city', 'description',
                  'github', 'image', 'experience_start_time', 'experience_end_time', 'experience_title',
                  'experience_description', 'education_end_year', 'education_place',
                  'education_title', 'completion_percentage']

    def get_completion_percentage(self, obj):
        return obj.get_completion_percentage()


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(
        queryset=MyUser.objects.all()
    )

    class Meta:
        model = Message
        fields = (
            'id',
            'sender',
            'content',
            'timestamp'
        )


class GroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=MyUser.objects.all()
    )
    messages = MessageSerializer(
        many=True, read_only=True
    )
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Group
        fields = ('id',
                  'name',
                  'members',
                  'messages',
                  'description',
                  'owner'
                  )


class GroupCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Group
        fields = ('id', 'name', 'members')


class GroupListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id', 'username')


class GroupSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'description')


class SearchSerializer(serializers.Serializer):
    users = UserSearchSerializer(many=True)
    groups = GroupSearchSerializer(many=True)


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentPostSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('text', 'group', 'parent', 'username')

    def create(self, validated_data):
        group = self.context['group']
        validated_data['group'] = group
        return super().create(validated_data)


class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('text',)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    username = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Comment
        fields = ("id", "username", "text", "children")


class GroupDetailSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        many=True,
    )
    messages = MessageSerializer(
        many=True,
        read_only=True
    )
    reviews = CommentSerializer(many=True)
    owner = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'owner',
            'members',
            'messages',
            'description',
            'reviews',
          )
