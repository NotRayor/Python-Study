import contact as ct

def run():
    print("Contact")
    contract_list = []
    while(1):
        menu = ct.print_menu()
        if menu == 1:
            cont = ct.set_contract()
            contract_list.append(cont)
        elif menu == 2:
            for i in contract_list:
                i.print_info()
        elif menu == 3:
            name = input("delete name : ")
            ct.delete_contract(contract_list, name)
        elif menu == 4:
            break


if(__name__ == "__main__"):
    run()
