class contact:
    def __init__(self, name, phoneNumber, email, addr):
        self.name = name
        self.phoneNumber = phoneNumber
        self.eMail = email
        self.addr = addr

    def print_info(self):
        print("==================================")
        print("이름 : " + self.name)
        print("핸드폰번호 : " + self.phoneNumber)
        print("이메일 : " + self.eMail)
        print("주소 : " + self.addr)

def set_contract():
    name = input("name : ")
    phoneNumber = input("Phone Number : ")
    eMail = input("eMail : ")
    addr = input("address : ")
    return contact(name,phoneNumber, eMail,addr);

def print_menu():
    print("1. set_contract")
    print("2. show list")
    print("4. Exit")
    menu = input("menu : ")
    return int(menu)

def delete_contract(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]




