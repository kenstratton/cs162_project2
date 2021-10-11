# phone
from classes import Phone

while True:
    # User input to create an instance
    print("Input info:")
    name = input("Your name: ")
    phone = input("Your phone number: ")
    if not str.isdigit(phone):
        print("[!] Phone number should be expressed in figures.\n")
        continue
    email = input("Your email address: ")

    if name and phone and email:
        phone = Phone(name, phone, email)
        break
    else:
        print("\n*Input of all items is required.")

# Instances to provide info for a user to try instance methods
p_j = Phone("Joseph", "111", "j@j.com")
p_d = Phone("Daniel", "222", "d@d.com")

print("\nInfo of imaginary friends:")
print("Name: {} PhoneNumber: {} Email: {}".format(
    p_j.user_name, p_j.phone_num, p_j.email_address))
print("Name: {} PhoneNumber: {} Email: {}".format(
    p_d.user_name, p_d.phone_num, p_d.email_address))

while True:
    # User input to manipulate the instance
    i = input("\nCommand Menu:\n[C]all\n[E]mail\n[H]istory\nE[x]it\n: ").lower()
    items = ["c", "e", "h", "x", "call", "email", "history", "exit"]
    if i in items:
        if i == "call" or i == "c":
            num = input("\nPut phone number: ")
            print(phone.call(num))
        elif i == "email" or i == "e":
            address = input("\nPut email address: ")
            text = input("Text messages:\n")
            print(phone.email(address, text))
        elif i == "history" or i == "h":
            hist_type = input("[C]all/[E]mail : Which history do you want to check? ").lower()
            hist_dict = phone.show_history(hist_type)
            if hist_dict["e"]:
                print(hist_dict["e"])
            else:
                for hist in hist_dict["hist_lis"]:
                    print(hist)
        elif i == "exit" or i == "x":
            print("\nGoobye!\n")
            break
    else:
        print("\n[!] Invalid input on the menu.")