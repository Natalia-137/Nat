#Класс прямогугольников, и 3 объекта, рассчитать площадь и периметр.

class Regtangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimetr(self):
        print(2 * (self.length + self.width))

a = Regtangle (2, 3)
b = Regtangle(55, 79)
c = Regtangle (32, 100)

a.area()
a.perimetr()
b.area()
b.perimetr()
c.area()
c.perimetr()


#Класс Math и стандартные математические действия над двумя переменными. проверка на объекте

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a*self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

one = Math(1, 5)

one.addition()
one.multiplication()
one.division()
one.subtraction()


#Описать кнопки на сайте DEMOQA. Атрибут тип - "Кнопка" - общий. Также атрибуты Название и локатор (по умолчанию пустой).
#Метод нажать кнопку выводит фразу "Клик по кнопке НАЗВАНИЕ КНОПКИ"


class Button:

    type: str = 'Кнопка'

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text}')

text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links_image = Button('Broken links - Image')
upload_and_download = Button('Upload and Download')
dynamic_properties = Button('Dynamic Properties')

print(text_box.text)
print(check_box.text)
print(radio_button.text)
print(web_tables.text)
print(buttons.text)
print(links.text)
print(broken_links_image.text)
print(upload_and_download.text)
print(dynamic_properties.text)
print('\n')
text_box.click()
check_box.click()
radio_button.click()
web_tables.click()
buttons.click()
links.click()
broken_links_image.click()
upload_and_download.click()
dynamic_properties.click()

