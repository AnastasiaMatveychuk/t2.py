from abc import ABC, abstractmethod

# Абстрактный класс Device
class Device(ABC):
    def __init__(self, implementation):
        self.implementation = implementation
        self.is_on = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Абстрактный класс DeviceImplementation
class DeviceImplementation(ABC):
    @abstractmethod
    def switch_channel(self):
        pass

    @abstractmethod
    def switch_station(self):
        pass

# Класс TV, представляющий конкретное устройство - телевизор
class TV(Device):
    def turn_on(self):
        print("Включение телевизора")
        self.is_on = True

    def turn_off(self):
        print("Выключение телевизора")
        self.is_on = False

    def switch_channel(self):
        print("Переключение каналов на телевизоре")

# Класс Radio, представляющий конкретное устройство - радио
class Radio(Device):
    def turn_on(self):
        print("Включение радио")
        self.is_on = True

    def turn_off(self):
        print("Выключение радио")
        self.is_on = False

    def switch_station(self):
        print("Переключение станций на радио")

# Класс Remote, представляющий пульт управления
class Remote:
    def __init__(self, device):
        self.device = device

    def power_on(self):
        self.device.turn_on()

    def power_off(self):
        self.device.turn_off()

    def switch_channel(self):
        self.device.implementation.switch_channel()

    def switch_station(self):
        self.device.implementation.switch_station()

# Класс для конкретной реализации устройства - телевизора
class TVImplementation(DeviceImplementation):
    def switch_channel(self):
        print("Переключение каналов на телевизоре")

    def switch_station(self):
        pass

# Класс для конкретной реализации устройства - радио
class RadioImplementation(DeviceImplementation):
    def switch_channel(self):
        pass

    def switch_station(self):
        print("Переключение станций на радио")

def main():
    tv = TV(TVImplementation())
    radio = Radio(RadioImplementation())

    while True:
        print("\nВыберите устройство:")
        print("1. Телевизор ({})".format("включен" if tv.is_on else "выключен"))
        print("2. Радио ({})".format("включено" if radio.is_on else "выключено"))
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if choice == '0':
            break
        elif choice == '1':
            device = tv
        elif choice == '2':
            device = radio
        else:
            print("Неверный выбор. Попробуйте снова.")
            continue

        remote = Remote(device)

        print("\nВыберите действие:")
        print("1. Включить")
        print("2. Выключить")
        print("3. Переключить канал/станцию")
        action = input("Ваш выбор: ")

        if action == '1':
            remote.power_on()
        elif action == '2':
            remote.power_off()
        elif action == '3':
            if device == tv:
                remote.switch_channel()
            elif device == radio:
                remote.switch_station()
        else:
            print("Неверное действие. Попробуйте снова.")

if __name__ == "__main__":
    main()


'''Этот код представляет реализацию паттерна "Мост" для управления устройствами (телевизором и радио) с помощью пульта управления.

Существуют абстрактные классы Device и DeviceImplementation, которые представляют устройства и их реализации соответственно. Класс Device имеет методы turn_on и turn_off, а класс DeviceImplementation имеет методы switch_channel и switch_station.

Классы TV и Radio представляют конкретные устройства (телевизор и радио) и реализуют методы включения, выключения и переключения каналов/станций.

Классы TVImplementation и RadioImplementation представляют конкретные реализации для телевизора и радио, соответственно. Они реализуют методы переключения каналов и станций.

Класс Remote представляет пульт управления, который может включать, выключать устройства и выполнять действия на них.

В функции main, пользователь может выбирать между телевизором и радио, включать, выключать устройства, а также переключать каналы (для телевизора) и станции (для радио). Состояние каждого устройства выводится при выборе и после каждого действия.

Этот код демонстрирует принцип "Мост", который позволяет отделять абстракцию (пульт управления) от реализации (устройства и их действий), что делает систему более гибкой и расширяемой.'''