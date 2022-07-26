from abc import ABCMeta, abstractmethod
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):
    def __init__(self, data) -> None:
        self.data = data

    @abstractmethod
    def save_file(self):
        raise NotImplementedError()


class SerializationBin(SerializationInterface):
     def save_file(self):
         with open("file.bin", "wb") as file:
             pickle.dump(self.data, file)


class SerializationJson(SerializationInterface):
     def save_file(self):
         with open("file.json", "wb") as file:
             json.dump(self.data, file)


class Meta(type):
     def __new__(smc, name, bases, attrs):
         attrs["class_number"] = Meta.children_number
         Meta.children_number += 1
         return type.__new__(smc, name, bases, attrs)


Meta.children_number = 0


class Cls1(metaclass=Meta):

     def __init__(self, data):
         self.data = data


class Cls2(metaclass=Meta):

     def __init__(self, data):
         self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)