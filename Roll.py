import random
import matplotlib.pyplot as plt

# تعداد بازیکنان را از کاربر دریافت می کنیم
num_players = int(input("Enter The number Of Players: "))

# یک لیست برای ذخیره اعداد تاس ایجاد می کنیم
dice_results = []
for i in range(300):
    dice_results.append(random.randint(1, 6))

# برای هر بازیکن یک لیست برای ذخیره نتایج پرتاب تاس ایجاد می کنیم
player_results = []
for i in range(num_players):
    player_results.append([])

# برای هر بازیکن، یک عدد تصادفی بین 1 تا 10 انتخاب می کنیم
for i in range(num_players):
    player_results[i].append(random.randint(1, 10))

# برای هر بازیکن، مراحل را تکرار می کنیم تا آخر لیست تاس
for i in range(num_players):
    current_index = player_results[i][0]
    while current_index < len(dice_results):
        player_results[i].append(dice_results[current_index])
        current_index += player_results[i][-1]

# برای هر بازیکن، خروجی را چاپ می کنیم
for i in range(num_players):
    print(f"Player {i} : \n", end=" ")
    for result in player_results[i]:
        print(result, end=" ")
    print('\n')

# Plotting the progress of each player
plt.figure(figsize=(10, 6))
for i in range(num_players):
    plt.plot(range(len(player_results[i])), player_results[i], label=f"Player {i}")

plt.title("Players' Progress")
plt.xlabel("Step")
plt.ylabel("Number")
plt.legend()
plt.grid(True)
plt.show()
