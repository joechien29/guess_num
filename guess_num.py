# 產生一個隨機變數，起始值/結束值讓使用者去設定
# 讓使用者重複輸入數字去猜
# 計算猜的次數
# 猜對的話，印出"猜對了"
# 猜錯的話，要告訴他比答案大/小


import random

start = input("請輸入隨機數字的起始值: ")
end = input("請輸入隨機數字的結束值: ")
start = int(start)
end = int(end)
r = random.randint(start, end)
print("***隨機出來的答案是: ", r, "***")

count = 0 # 請算猜的次數
while True:
    count += 1
    guess_int = input("請輸入你猜的數字: ")
    guess_int = int(guess_int)
    if guess_int == r:
        print("猜對了")
        print("你已經猜了", count, "次")
        break
    elif guess_int > r:
        print("你的數字比答案大")
    elif guess_int < r:
        print("你的數字比答案小")
    print("你已經猜了", count, "次")
            
       