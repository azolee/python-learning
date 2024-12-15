class Person:
    name: str = None
    age: int = None

    def __init__(self, name: str = None, age: int = None) -> None:
        self.name: str = name if name is not None else 'John Doe'
        self.age: int = age if age is not None else 0

    def greet(self) -> str:
        age: str = self.age > 0 and f'{self.age} years old.' or 'ageless.'
        return f'Hello, my name is "{self.name}" and I am {age}'

    def __str__(self) -> str:
        return self.greet()

print(Person(name='Zoli', age=45))
print(Person())
