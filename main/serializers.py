from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from main.models import NetworkUnit, Contact, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class NetworkUnitSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = NetworkUnit
        fields = '__all__'

    def validate(self, data):
        if 'debt' in data:
            raise serializers.ValidationError('Поле "debt" можно задать только через админ панель.')
        return data



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token