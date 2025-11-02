def check_status(status_code):
    print("Status code: ", status_code)
    if status_code == 200:
        return "PASS"
    elif status_code == 400 or status_code == 500:
        return "FAIL"
    else:
        return "UNKNOWN"


code = int(input("enter the status code: "))
print(check_status(code))  # UNKNOWN
# Example Test Cases
# print(check_status(200))  # PASS
# print(check_status(500))  # FAIL
# print(check_status(302))  # UNKNOWN
