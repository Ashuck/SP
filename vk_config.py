from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from DB_Worker import Worker


W = Worker()
token = "f5396d49d9cdf036623a10ecfb71c6252b0afa0c912a65a79c44c3001e236a18f53fd72630206e4587d50"


t = W.get_themes()
# Клавиатуры
Kbr = VkKeyboard()
from_inline = {}
for theme in t:
    Kbr.add_button(theme[0], color=VkKeyboardColor.PRIMARY)
    if theme != t[-1]:
        Kbr.add_line()
    ans = W.get_answers(theme[0])
    kbr_schet = VkKeyboard(inline=True)
    for line in ans:
        kbr_schet.add_button(line[0], color=VkKeyboardColor.SECONDARY)
        if line != ans[-1]:
            kbr_schet.add_line()

    for line in ans:
        from_inline[line[0]] = {
            "text": line[1],
            "kbr": kbr_schet.get_keyboard()
        }

