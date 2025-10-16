# Automation test case comparison with user input
# Ignores spaces and letter case

expected_title = input("Enter Expected Title: ")
actual_title = input("Enter Actual Title: ")

# Normalize inputs: remove extra spaces and ignore case
if expected_title.strip().lower() == actual_title.strip().lower():
    print("✅ Test Case Passed")
else:
    print("❌ Test Case Failed")
    print(f"Expected: '{expected_title}'")
    print(f"Actual_Result:   '{actual_title}'")
