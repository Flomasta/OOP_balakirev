class ImageFileAcceptor:
    def __init__(self, extentions):
        self.extentions = extentions

    def __call__(self, *args, **kwargs):
        return args[0].split('.')[-1] in self.extentions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/JIQhCEqb4rU
#
# Подвиг 3. Для последовательной обработки файлов из некоторого списка, например:
#
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
# Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с указанными расширениями.
#
# Для этого предполагается создавать объекты класса командой:
#
# acceptor = ImageFileAcceptor(extensions)
# где extensions - кортеж с допустимыми расширениями файлов, например: extensions = ('jpg', 'bmp', 'jpeg').
#
# А, затем, использовать объект acceptor в стандартной функции filter языка Python следующим образом:
#
# image_filenames = filter(acceptor, filenames)
# Пример использования класса (эти строчки в программе писать не нужно):
#
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
# P.S. Ваша задача только объявить класс ImageFileAcceptor. На экран ничего выводить не нужно.
