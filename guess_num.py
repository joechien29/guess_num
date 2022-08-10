# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話，印出"猜對了"
# 猜錯的話，要告訴他比答案大/小


import random

r = random.randint(1, 100)
guess_int = input("輸入你猜的數字")
guess_int = int(guess_int)
print("隨機出來的答案是: ",r)

i = 10

while i > 0:
    i = i - 1
    if guess_int == r:
        print("猜對了")
        break
    else:
        if i > 0:
            print("你還有", i, "次機會")
            guess_int = input("請輸入你猜的數字: ")
            guess_int = int(guess_int)
            if guess_int > r:
                print("你的數字比答案大")
            elif guess_int < r:
                print("你的數字比答案小")
        else:
            print("遊戲結束")
            
       