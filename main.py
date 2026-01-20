tsez_dict = {
    "Солнце": "Бухъ",
    "Луна": "Буци",
    "Земля": "Чlедо",
    "Вода": "Лъи",
    "Огонь": "Цlи",
    "Воздух": "Муши",
    "День": "Гъуди",
    "Ночь": "Неширу",
    "Камень": "Гъlула",
    "Трава": "Бих",
}

reverse_dict = {v: k for k, v in tsez_dict.items()}

change_lang = input("Выберите язык ввода 'ru' или 'ddo': ").strip().lower()

if change_lang == "ru":
    word = input("Введите слово на русском: ").strip().capitalize()
    if word in tsez_dict:
        print(f"Перевод: {tsez_dict[word]}")
    else:
        print("Введенное слово не найдено!")

elif change_lang == "ddo":
    word = input("Цахо рожи: ").strip().capitalize()
    if word in reverse_dict:
        print(f"Рутни: {reverse_dict[word]}")
    else:
        print("Цахру рожи ресунчlу!")
else:
    print("Ошибка выбора языка.")
    