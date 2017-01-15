# -*- coding:utf-8

# 首先，創建一個待驗證用戶列表
# 和一個用於儲存已驗證用戶的空列表。
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 驗證每個用戶，直到沒有未驗證用戶為止
# 將每個經過驗證的列表都移到已驗證用戶列表中

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print("Verifying user: " + current_users.title())
    confirmed_users.append(current_users)

# 顯示所有已驗證的用戶
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())