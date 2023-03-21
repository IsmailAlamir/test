from rest_framework import serializers

from accounts.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    print(serializers.ModelSerializer)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2','first_name','last_name']
        extra_kwargs = {
				'password': {'write_only': True},
                'first_name': {'required': True},
                'last_name': {'required': True},
		}

    def	save(self):
        account = CustomUser(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
				)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        print(account)
        account.save()

        return account

# get user information
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"













