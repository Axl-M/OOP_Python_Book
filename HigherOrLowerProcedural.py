# Карточная игра «Больше-меньше»

import random

# Константы карт
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8


# Проходим по колоде, и эта функция возвращает случайную карту из колоды
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard


# Проходим по колоде, и эта функция возвращает перемешанную копию колоды

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # создаем копию стартовой колоды
    random.shuffle(deckListOut)
    return deckListOut


# Основной код
print('\nДобро пожаловать в игру "БОЛЬШЕ или МЕНЬШЕ.')
print('Вам надо выбрать будет ли следующая карта больше или меньше чем эта карта')
print('За правильный ответ начисляется 20 очков. За неправильный снимается 15 очков')
print('Сейчас у вас есть 50 очков.')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # несколько игр
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):  # играем в одну игру из этого количества карт
        answer = input('Следующая карта будет БОЛЬШЕ или МЕНЬШЕ чем ' +
                       currentCardRank + currentCardSuit + '? (Введите + or -): ')
        answer = answer.casefold()  # переводим в нижний регистр
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Следующая карта:', nextCardRank + ' ' + nextCardSuit)
        if answer == '+':
            if nextCardValue > currentCardValue:
                print('Вы угадали')
                score = score + 20
            else:
                print('Простите, но она не БОЛЬШЕ')
                score -= 15

        elif answer == '-':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('Вы угадали')
            else:
                score -= 15
                print('Извините, но она НЕ МЕНЬШЕ')
        print('Ваш счет:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # не нужна текущая масть

    goAgain = input('Чтобы играть ещё раз нажмите ENTER, or "q" чтобы выйти: ')

    if goAgain == 'q':
        break

print('Пока...')
