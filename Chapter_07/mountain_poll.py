# -*- coding:utf-8

responses = {}

# 設置一個標誌，指出調查是否繼續
polling_active = True

while polling_active :
    # 提示輸入被調查者的名字和回答
    name = str(input("\nWhat's your name? "))
    response = str(input("Which mountain would you like to climb someday? "))

    # 將答案儲存在字典中
    responses[name] = response

    # 看看是否還有人要參與調查
    repeat = str(input("Would you like to let another person respond? (yes / no) "))
    if repeat == 'no':
        polling_active = False

# 調查結束，顯示結果
print("\n---- Poll Results ----")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")

