# API Response Tester with Complete Edge Case Handling

response = int(input("Enter API response code: "))

if response < 100 or response > 599:
    print(f"⚠️ Invalid Response Code ({response}) - Valid range is 100 to 599")
elif response == 200:
    print("✅ Passed API Request")
elif response == 201:
    print("✅ Resource Created Successfully (201)")
elif response == 204:
    print("✅ Request Successful but No Content (204)")
elif response == 400:
    print("❌ Bad Request (400) - Check your input data")
elif response == 401:
    print("❌ Unauthorized (401) - Authentication required")
elif response == 403:
    print("❌ Forbidden (403) - Access denied")
elif response == 404:
    print("❌ Failed API Request - Not Found (404)")
elif response == 500:
    print("❌ Internal Server Error (500)")
elif response == 503:
    print("❌ Service Unavailable (503)")
else:
    print(f"⚠️ Unknown the Response Code: {response}")
