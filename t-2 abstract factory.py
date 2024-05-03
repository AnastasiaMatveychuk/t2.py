#Работу выполнела Матвейчук Анастасия ПИ22-1в
#Использование паттерна абстрактная фабрика, применяется с заданием Шахматы
class Chessman:
    def info(self):
        pass
# Базовый класс для шахматных фигур

class Pawn(Chessman):
    def info(self):
        print("Pawn")


class Rook(Chessman):
    def info(self):
        print("Rook")


class Queen(Chessman):
    def info(self):
        print("Queen")
# Классы для конкретных шахматных фигур (пешка, ладья, ферзь)

class ChessFactory:
    def createPawn(self):
        pass

    def createRook(self):
        pass

    def createQueen(self):
        pass
# Абстрактная фабрика для создания шахматных фигур

class WhiteChessFactory(ChessFactory):
    def createPawn(self):
        return Pawn()

    def createRook(self):
        return Rook()

    def createQueen(self):
        return Queen()
# Фабрика для создания белых шахматных фигур

class BlackChessFactory(ChessFactory):
    def createPawn(self):
        return Pawn()

    def createRook(self):
        return Rook()

    def createQueen(self):
        return Queen()
# Фабрика для создания черных шахматных фигур

class Chess:
    def __init__(self):
        self.pawns = []
        self.rooks = []
        self.queens = []

    def info(self):
        for pawn in self.pawns:
            pawn.info()
        for rook in self.rooks:
            rook.info()
        for queen in self.queens:
            queen.info()
# Класс, представляющий шахматную доску

class Game:
    def createChess(self, factory):
        chess = Chess()
        chess.pawns.append(factory.createPawn())
        chess.rooks.append(factory.createRook())
        chess.queens.append(factory.createQueen())
        return chess
# Класс для создания игры и шахматных фигур

game = Game()
white_factory = WhiteChessFactory()
black_factory = BlackChessFactory()
# Создание игры и фабрик для белых и черных шахматных фигур

white_chess = game.createChess(white_factory)
black_chess = game.createChess(black_factory)
# Создание шахмат для белых и черных

print("White Chess:")
white_chess.info()

print("\nBlack Chess:")
black_chess.info()
# Вывод информации о шахматах
