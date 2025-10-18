# import random
# import time
#
# timeout = 5
#
# second = 1
# while second <= timeout:
#     # 30% chance the page loads each second
#     if random.random() < 0.3:
#         print(f"Page loaded successfully in {second} seconds!")
#         break
#     print(f"Second {second}: Page still loading...")
#     second += 1
#     time.sleep(1)
# else:
#     print("Timeout! Page did not load within 5 seconds.")

# page_loaded = False
# wait_time = 0
# timeout = 5
#
# while wait_time < timeout:
#     # Ask user if the page has loaded
#     user_input = input(f"Second {wait_time + 1}: Has the page loaded? (yes/no): ").lower()
#
#     if user_input == "yes":
#         page_loaded = True
#
#     if page_loaded:
#         print(f"Page loaded successfully in {wait_time + 1} seconds!")
#         break
#
#     wait_time += 1
# else:
#     print("Timeout! Page did not load within 5 seconds.")


import random
import time

timeout = 5

second = 1
while second <= timeout:
    # 30% chance the page loads each second
    if random.random() < 0.3:
        print(f"Page loaded successfully in {second} seconds!")
        break
    print(f"Second {second}: Page still loading...")
    second += 1
    time.sleep(1)
else:
    print("Timeout! Page did not load within 5 seconds.")
