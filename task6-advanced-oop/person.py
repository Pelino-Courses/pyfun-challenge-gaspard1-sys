from abc import ABC, abstractmethod



class Person(ABC):
    

    def __init__(self, name: str, id_number: str) -> None:
        self.name = name
        self.id_number = id_number

    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.get_role()}: {self.name} (ID: {self.id_number})"
