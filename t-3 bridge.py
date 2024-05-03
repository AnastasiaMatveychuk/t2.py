#Работу выполнила Матвейчук Анастасия ПИ22-1в
#Использование паттерна мост применяемый к задаче связанные устройства телевизор и радио, с помощью пульта управления
from abc import ABC, abstractmethod

# Абстрактный класс Device
class Device(ABC):
    def __init__(self, implementation):
        self.implementation = implementation

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Абстрактный класс DeviceImplementation
class DeviceImplementation(ABC):
    @abstractmethod
    def perform_action(self):
        pass

# Класс TV, представляющий конкретное устройство - телевизор
class TV(Device):
    def turn_on(self):
        print("Включение телевизора")
        self.implementation.perform_action()

    def turn_off(self):
        print("Выключение телевизора")

# Класс Radio, представляющий конкретное устройство - радио
class Radio(Device):
    def turn_on(self):
        print("Включение радио")
        self.implementation.perform_action()

    def turn_off(self):
        print("Выключение радио")

# Класс Remote, представляющий пульт управления
class Remote:
    def __init__(self, device):
        self.device = device

    def power_on(self):
        self.device.turn_on()

    def power_off(self):
        self.device.turn_off()

# Класс для конкретной реализации устройства - телевизора
class TVImplementation(DeviceImplementation):
    def perform_action(self):
        print("Переключение каналов на телевизоре")

# Класс для конкретной реализации устройства - радио
class RadioImplementation(DeviceImplementation):
    def perform_action(self):
        print("Переключение станций на радио")

def main():
    tv = TV(TVImplementation())
    radio = Radio(RadioImplementation())

    remote_tv = Remote(tv)
    remote_radio = Remote(radio)

    remote_tv.power_on()
    remote_tv.power_off()

    remote_radio.power_on()
    remote_radio.power_off()

if __name__ == "__main__":
    main()