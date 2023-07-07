from rest_framework import serializers
from .models import Account,Profile

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','password','username']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self,request):
        if request.user:
            user = Account(email=self.validated_data['email'],username = self.validated_data['username'])
            user.set_password(self.validated_data['password'])
            user.save()
            
        
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email','username']

class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'