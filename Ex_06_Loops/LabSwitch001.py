
# def check_number(x):
#     match x:
#         case 10:
#             print("it's 10")
#         case 25:
#             print("it's 25")
#         case _:
#             print("it's neither 10 be 25")
#
# check_number(10)
# check_number(25)

def num_check(num):
    match num:
        case   10 | 20 | 30 | 40 | 50 :
            print(f"matched: {num}")
        case _:
            print(f"not matched: {num}")
num_check(10)
num_check(20)
num_check(30)
num_check(400)



