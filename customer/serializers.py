from rest_framework import serializers
from .models import Customer,Review
from django.contrib.auth.models import User
from customer.constants import USER_TYPE_CHOICES
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    # Include the nested UserSerializer to update the User fields
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ['user', 'image', 'phone', 'address', 'user_type']

    def update(self, instance, validated_data):
        # Extract the user data
        user_data = validated_data.pop('user', None)

        # Update the User model fields
        if user_data:
            user_serializer = UserSerializer(instance=instance.user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()

        # Update the remaining Customer fields
        instance.image = validated_data.get('image', instance.image)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.save()

        return instance
    
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = ['id','reviewer','pet','body','rating','created_on',]
        read_only_fields = ['id','reviewer','created_on',]

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password',]

    def save(self, **kwargs):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error': "Passwords don't match"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})

        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_active = False  
        user.save()
 
        customer = Customer(user=user)
        print(customer)
        customer.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True,write_only=True)
    new_password = serializers.CharField(required=True,write_only=True)

    def validate_new_password(self,value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value
    
    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({"old_password":"Old password is incorrect."})
        return data





