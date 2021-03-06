from math import floor, ceil
import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
    '''Каждый раз при угадывании выбрасывается часть, в которой точно нет нужного числа'''
    predict = np.random.randint(1,101)
    count = 1
    a=1
    b=101
    while number != predict:
        if number > predict:
            a = predict
        else:
            b = predict
        predict = np.random.randint(a,b)
        count+=1
    return count
   
def game_core_v4(number):
    """При каждой итеграции в цикле while смещаются границы возможного нахождения числа, если границы совпали
    -значит, угадываемое числа - одна из границ"""
    bottom = 0
    top = 100
    count = 1
    while bottom != top:
        # ты не можешь совершать операции с number, тебе же он неизвестен! :)
        # так-то можно было predict = number написать и закончить.
        sep = number - bottom
        half = ceil((top-bottom)/2)
        if sep > half:
            bottom += half
        elif sep < half:
            top -= half
        elif sep == half:
            bottom = bottom + sep
    # тут у тебя заканчивается всё тем, чето bottom == number
    predict = bottom
    while predict != number:
        predict += 1
        count += 1
    return count

def game_core_v5(number):
    """ Перед каждым следующим угадыванием границы возможного нахождения числа дважды смещаются
    Это то же, что game_core_v4, только там границы смещаются до угадывания числа. Добавил так как 
    не уверен в правильности game_core_v4"""
    predict = np.random.randint(1,101)
    count = 1
    a=1
    b=101
    while number != predict:
        if number > predict:
            a = predict
            middle = a + ((b-a)/2)
            # ну так не честно! :)  ты за один цикл делаешь две операции проверки, а считаешь как один count.
            if number == int(middle):
                predict = int(middle)
                break
            if number > middle:
                a = floor(middle) + 1 
            elif number < middle:
                b = ceil(middle)
        else:
            b = predict
            middle = a + ((b-a)/2)
            if number == int(middle):
                predict = int(middle)
                break
            if number < middle:
                b = ceil(middle)
            elif number > middle:
                a = floor(middle) + 1 
        predict = np.random.randint(a,b)
        count+=1
    return count

def game_core_v5_se(number):
    """Бинарный поиск number в диапазоне от minimum до maximum"""
    count   = 0
    mininum = 1
    maximum = 100
    
    while True:
        count += 1
        predict = (mininum+maximum)//2
        if predict == number:
            return count
        elif number > predict:
            mininum = predict + 1
        else:
            maximum = predict - 1

if __name__ == "__main__":
    print('-'*4, 'game_core_v3', '-'*4)
    score_game(game_core_v3)
    print()

    print('-'*4, 'game_core_v4', '-'*4)
    score_game(game_core_v4)
    print()

    print('-'*4, 'game_core_v5', '-'*4)
    score_game(game_core_v5)
    print()

    print('-'*4, 'game_core_v5_se', '-'*4)
    score_game(game_core_v5_se)
    print()