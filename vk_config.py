from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "f5396d49d9cdf036623a10ecfb71c6252b0afa0c912a65a79c44c3001e236a18f53fd72630206e4587d50"

# Клавиатуры
Kbr = VkKeyboard()
Kbr.add_button('Проверки счетной палаты', color=VkKeyboardColor.PRIMARY)

kbr_schet = VkKeyboard(inline=True)

btns = [
    ("Документы", "Сроки"), 
    ("Что проверяют", "Регламент")
]

for line in btns:
    for btn in line:
        kbr_schet.add_button(btn, color=VkKeyboardColor.SECONDARY)
    if line != btns[-1]:
        kbr_schet.add_line()

