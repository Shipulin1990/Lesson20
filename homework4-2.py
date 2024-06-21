def test_function():
    def inner_function():
        inner_function("Я в области видимости функции test_function")
        print(inner_function("Я в области видимости функции test_function"))
    print(inner_function("Я в области видимости функции test_function"))


inner_function("Я в области видимости функции test_function")
# Выдает ошибку "Имя не определено", поскольку мы вызываем функцию вне области, в которой она указана
