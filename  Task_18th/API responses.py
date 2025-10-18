# 🧠 Explanation
#
# attempt = 1 → counter for how many tries we’ve done.
#
# while attempt <= max_attempts: → loop until max 3 tries.
#
# response_code = random.choice([200, 500, 502]) → simulates API response (replace this with your real API call).
#
# if response_code == 200: → success → break the loop.
#
# else: → increment attempt and retry.
#
# else: after while loop → runs if loop ends without break, i.e., all retries failed.

# import random  # to simulate API responses
#
# max_attempts = 3
# attempt = 1
#
# while attempt <= max_attempts:
#     # Simulate API response (for testing)
#     response_code = random.choice([200, 500, 502])  # random response
#
#     print(f"Attempt {attempt}: Response {response_code}")
#
#     if response_code == 200:
#         print("✅ API call succeeded!")
#         break
#     else:
#         attempt += 1
# else:
#     print("❌ API call failed after 3 attempts.")
# ----------------------------------------------------------------

max_attempts = 3
attempt = 1

while attempt <= max_attempts:
    response_code = int(input(f"Enter response code for attempt {attempt}: "))
    print(f"Attempt {attempt}: Response {response_code}")

    if response_code == 200:
        print("API call succeeded!")
        break
    attempt += 1
else:
    print("API call failed after 3 attempts.")
