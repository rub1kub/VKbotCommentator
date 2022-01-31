import vk_api
import time
import random


def intro():
    print("")
    print("     **********************************************************          ")
    print("")
    print("           Страничный Бот-комментатор для ВКонтакте.       ")
    print("  Developer: vk.com/dmitry_puzik | GitHub: github.com/LordRubikI")
    print("")
    print("     **********************************************************          ")
    print("")


def captcha_handler(captcha):
    key = input("Введи код капчи {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def func():
    try:
        token = input("Токен пользователя: ")
        user = input("Введите id пользователя на стене у которого находится пост: ")
        post = input("Введите id записи: ")
        sumrandom = input("Сколько вариаций комметариев: ")
        text_com = []
        for i in range(int(sumrandom)):
            text_com.append(str(input(f"Введи комметарий №{i}: ")))
        comms = input("Сколько накрутить комментариев: ")
        times = input("Введите задержку перед отправкой комментария: ")

        session = vk_api.VkApi(token=token,captcha_handler=captcha_handler)

        comms = int(comms)
        num = 0

        while num < comms:
            session.method("wall.createComment", {
                "owner_id": user,
                "post_id": post,
                "message": random.choice(text_com),
            })
            time.sleep(int(times))
            print(f"Добавлено: {num} " + "комментариев" + "\r")
            num += 1

            if num == comms:
                print("Все комментарии добавлены!")
                break
    except vk_api.exceptions.ApiError as error:
        error = str(error)
        if error[1:4] == "100":
            print("Пост отсутствует")
        elif error[1:2] == "5":
            print("Ошибка авторизации")
        elif error[1:4] == "213":
            print("Нет доступа к записи")
    except vk_api.exceptions.Captcha:
        print("Обнаружена капча! Увеличьте время задержки между отправкой комметариев\n"
              "или добавьте больше вариаций сообщений.")


intro()
func()
