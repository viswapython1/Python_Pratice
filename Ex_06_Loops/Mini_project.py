# QA Test Menu Tool using match-case

print("=== 🧪 QA TEST MENU TOOL ===")
print("1️⃣  Check API Response")
print("2️⃣  Login Validation")
print("3️⃣  Compare Expected vs Actual Output")
print("4️⃣  Tester Notes")
print("5️⃣  Exit")

while True:
    choice = input("\nEnter your choice (1-5): ")

    match choice:
        case "1":
            code = int(input("Enter API Response code: "))
            match code:
                case 200 | 201 | 204:
                    print("✅ API Test Passed (Success)")
                case 400 | 401 | 403:
                    print("❌ Client Error - Check Request or Auth")
                case 500 | 502 | 503:
                    print("⚠️ Server Error - Try Again Later")
                case _:
                    if code < 100 or code > 599:
                        print("🚫 Invalid Code Range (Valid 100–599)")
                    else:
                        print("🔍 Unknown Code, Manual Check Required")

        # ✅ Option 2: Login Validation
        case "2":
            correct_user = "admin"
            correct_pass = "12345"
            user = input("Enter Username: ").strip().lower()
            pwd = input("Enter Password: ").strip()

            if user == correct_user and pwd == correct_pass:
                print("login success")
            else:
                print("login failed")

        case "3":
            expected = input("Enter Expected Value: ").strip()
            actual = input("Enter Actual Value: ").strip()
            if expected.lower() == actual.lower():
                print("✅ Test Case Passed")
            else:
                print("❌ Test Case Failed")
                print(f"Expected: '{expected}'")
                print(f"Actual:   '{actual}'")

        case "4":

            print("🗒️  Tester Tips:")
            print(" - Always test with valid, invalid, and boundary values.")
            print(" - Normalize inputs (use .strip() and .lower()).")
            print(" - Log results clearly in your reports.")
            print(" - Automate repetitive checks.")

            # ✅ Exit
        case "5":

            print("👋 Exiting QA Test Menu Tool... Goodbye!")
            break

        # ⚠️ Invalid Choice
        case _:
            print("⚠️ Invalid Option! Please enter a number between 1–5.")
