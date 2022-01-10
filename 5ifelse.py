answer = input("Идет ли сейчас дождь?: ")
if str.lower(answer) == "да":
    answer2 = input("Ветренно ли на улице?: ")
    if str.lower(answer2) == "да":
        print("Слишком ветрено для зонта!")
    else:
        print("Возьми зонт!")
else:
    print("Хорошего дня!")

