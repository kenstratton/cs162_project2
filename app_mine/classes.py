import datetime

phone_lis = []

class Phone(object):
    def __init__(self, user_name, phone_num, email):
        self.user_name = user_name
        self.phone_num = phone_num
        self.email_address = email
        self.history = {"call":[], "email":[]}
        phone_lis.append(self)

    # Search another instance based on user input and insert a record into its History property (key: call).
    def call(self, num):
        for phone in phone_lis:
            if num == phone.phone_num:
                now = datetime.datetime.now()
                phone.history["call"].append({"name":self.user_name, "num":self.phone_num, "date":now.strftime("%m/%d/%Y %H:%M")})
                return "Connected!"
                break
        else:
            return "[!] The number you called is no longer in service."

    # Search another instance based on user input and insert a record into its History property (key: email).
    def email(self, address, text):
        if text:
            for phone in phone_lis:
                if address == phone.email_address:
                    now = datetime.datetime.now()
                    phone.history["email"].append({"address":self.email_address, "text":text, "date":now.strftime("%m/%d/%Y %H:%M")})
                    return "Successfully sent!"
                    break
            else:
                return "[!] The address doesn\'t exist."
        else:
            return "[!] Text shoud not be empty."

    # Show records of calls and emails which other instances might send to this instance.
    def show_history(self, i):
        hist_dict = {"hist_lis":[],"e":None}
        if i == "call" or i == "c":
            if self.history["call"]:
                for hist in self.history["call"]:
                    hist_dict["hist_lis"].append("From {} {}, {}".format(hist['name'],hist['num'],hist['date']))
            else:
                hist_dict["e"] = "[!] There is no call history."
        elif i == "email" or i == "e":
            if self.history["email"]:
                for hist in self.history["email"]:
                    hist_dict["hist_lis"].append("From {}, {}\n{}:".format(hist['address'],hist['date'],hist['text']))
            else:
                hist_dict["e"] = "[!] There is no mail history."
        else:
            hist_dict["e"] = "[!] Your input was inappropriate."

        return hist_dict