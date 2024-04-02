from kbds.keyboards import get_kb


def check_wallet_address():
    pass

def get_main_kb():
    return get_kb('Кошелек/Wallet👛',
                       'Баланс/balance🐹',
                       'Twitter(HOT)📢',
                       'Условия/Terms📒',
                       placeholder='Выберай кнопку',
                       sizes=(2, 2,)
           )
