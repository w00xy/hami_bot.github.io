from kbds.inline import get_url_btns
from kbds.keyboards import get_kb


def get_main_kb():
    return get_kb('Кошелек/Wallet👛',
                       'Баланс/balance🐹',
                       'Twitter(BONUS)📢',
                       'Условия/Terms📒',
                       placeholder='Выберай кнопку',
                       sizes=(2, 2,)
           )

def get_invite_kb(ref_link):
    text = "500 $HAMI for everybody🐹\nLet's grow the biggest community ever!"
    return get_url_btns(btns={
                    'Пригласить друга/invite👥' : f'https://t.me/share/url?url={ref_link}&text={text}',
                 }
    )
