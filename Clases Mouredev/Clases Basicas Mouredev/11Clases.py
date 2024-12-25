"""     CLASES      """

#definir una clase 
#las clases inician con mayuscula al inicio de cada palabra
class Pass:
    #funciona para ejecutar una clase pero que no haga nada 
    pass
#si una clase tiene pass es que en verdad no la necesitas 


print(Pass)
print(Pass())

class Person:
    #_init_ es una palabra reservada para crear clases 
    #init se usa para que el sistema entienda que se esta creando una clase y se establcen los valores relacionados a la clase 
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
        #usamos self para referirse a si mismo, usar self.name se refiere al valor name que requiere la clase 
        #las propiedades que creamos y pasan a existir fuera de la clase es lo que ponems despues de self. 

my_person = Person('Fidel', 'Pizart')
print(my_person.name)\

class Person2:
    def __init__(self, name, surname):
        self.full_name= f'{name} {surname}'

    def caminar(self):
        print(f'{self.full_name} esta caminando')


my_person2=Person2('Aleandro', 'Perez')
print(my_person2.full_name)

my_person2.caminar()

