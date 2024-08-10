from rest_framework import serializers

# EXAMPLE!!!!!


class MySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

serializer = MySerializer(data={'name': 'John Doe', 'email': 'john@example.com'})

if serializer.is_valid():
    # Access validated data
    validated_data = serializer.validated_data
    print(validated_data)
