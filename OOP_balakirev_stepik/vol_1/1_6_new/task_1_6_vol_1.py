class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return ("Ошибка: нельзя создавать объекты абстрактного класса")


obj = AbstractClass()


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7aVqWfrAdqw
#
# Подвиг 6. Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:
#
# obj = AbstractClass()
# переменная obj должна ссылаться на строку с содержимым:
#
# "Ошибка: нельзя создавать объекты абстрактного класса"
#
# P.S. В программе объявить только класс, выводить на экран ничего не нужно.
