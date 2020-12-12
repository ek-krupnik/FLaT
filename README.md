# Formal Languages and Translations
Решение задачи:

   (Вариант 10)

   Даны А (регулярное выражение в обратной польской записи), буква x и натуральное число k. Вывести длину кратчайшего 
   слова из языка L, содержащего суффикс x**k.

Реализованный алгоритм:
   1) Приведение регулярного выражения из обратной польской нотации к привычному виду (для упрощения интуитивного 
   понимания)
   2) Создание недетерминированного конечного автомата с однобуквенными переходами из полученного регулярного выражения 
   (оставляем эпсилон-переходы, за счет этого имеем только одно терминальное состояние)
   3) Инвертирование рёбер автомата (в том числе начальная вершина теперь считается терминальной и наоборот), теперь 
   решаем эквивалентную задачу - нахождение кратчайшего слова, содержащего требуемый префикс
   4) По построенному автомату идем BFS-ом, далее ответ находится тривиально.
   
Запуск code coverage:
   1) Возможно, потребуется установить coverage модуль для Python (pip install coverage)
   2) Команда coverage run test.py - делает все необходимое
   3) Визуализация результата: coverage html
