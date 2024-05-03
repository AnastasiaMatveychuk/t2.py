#Работу выполнила Матвейчук Анастасия ПИ22-1в
#Использование паттерта Command применяется к заданию реализация транзакций
class Transaction:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()


class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class CreateGameCommand(Command):
    def __init__(self, game):
        self.game = game

    def execute(self):
        self.game.create()

    def undo(self):
        # Реализуйте отмену операции создания игры (если необходимо)
        pass


class MakeMoveCommand(Command):
    def __init__(self, game, move):
        self.game = game
        self.move = move

    def execute(self):
        self.game.make_move(self.move)

    def undo(self):
        # Реализуйте отмену операции хода (если необходимо)
        pass


# Пример использования
class Game:
    def create(self):
        print("Создание игры")

    def open(self, file):
        print(f"Открытие игры из файла {file}")

    def save(self, file):
        print(f"Сохранение игры в файл {file}")

    def make_move(self, move):
        print(f"Ход: {move}")

def main():
    game = Game()
    transaction = Transaction()

    # Создаем команды и добавляем их в транзакцию
    transaction.add_command(CreateGameCommand(game))
    transaction.add_command(MakeMoveCommand(game, "Ход 1"))
    transaction.add_command(MakeMoveCommand(game, "Ход 2"))

    # Выполняем транзакцию
    transaction.execute()

    # Отменяем транзакцию
    transaction.undo()

if __name__ == "__main__":
    main()