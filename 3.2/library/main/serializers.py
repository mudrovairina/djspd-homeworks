from rest_framework import serializers

from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = "__all__"

    #доп задание
    def to_representation(self, book):
        representation = super().to_representation(book)
        representation['orders_count'] = book.order_set.count()
        return representation


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = "__all__"

    #доп задание
    def to_representation(self, order):
        representation = super().to_representation(order)
        books = order.books.all()
        serializer = BookInOrdersSerializer(books, many=True)
        representation['books'] = serializer.data
        return representation


class BookInOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["author", "title", "year"]