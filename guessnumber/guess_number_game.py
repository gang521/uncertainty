import random
def guess_number():
    target_number = random.randint(1, 100)
    chances = 5

    while chances >= 0:
        guess = int(input("请猜一个1到100的数字,需要是整数哦┗|｀O′|┛ 嗷~~喵^_^："))

        if guess > target_number:
            print("哈哈哈，偏大啦，主人还有{}次机会啦喵".format(chances))
        elif guess < target_number:
            print("偏小啦，主人还有{}次机会啦喵".format(chances))
        else:
            print("哼，居然被主人猜中了喵，但是小甜甜喵是不会认输的喵")
            return

        chances -= 1

    print("略略略主人已经没有机会啦喵，想不到吧答案是{}喵^".format(target_number))

guess_number()