
import schedule
vending_machine = {"General Medicine": "G", "ENT": "E",
                   "Orthopedics": "O", "Pediatrics": "P", "Cardiac Science": "C"}

doctor_list = {'G': {'JD': 'Dr. John Doe', 'MD': 'Dr. Manoj Dwivedi', 'SR': 'Dr. Shlok Raut'},
               'E': {'PS': 'Dr. Prajct Sao', 'SM': 'Dr. Sunita More', 'AAJ': 'Dr. Abhishek Arun Jaiswal'},
               'O': {'RG': 'Dr. Rahul Gupta', 'AV': 'Dr. Amit Vatkar', 'SK': 'Dr. Santosh Kondekar'},
               'PA': {'PA': 'Dr. Paras Agarwal', 'SC': 'Dr. Sandeep Cheruku', 'MG': 'Dr. Manish Gupta'},
               'C': {'AP': 'Dr. Amruta Prabhu', 'HM': 'Dr. Hasmukh Mehta', 'SN': 'Dr. Saleem Naik'}}

token_number = 100
sessionStorage = {}


def update_token():
    global token_number
    token_number += 1


def reset_token():
    global token_number
    token_number = 100


schedule.every(24).hours.do(reset_token)


def call_next_patient():
    import os
    os.system('spd-say "next patient please"')


def main():
    item_list = []
    switch = 1
    print()
    print('**********************-----------**************************')
    print("***** Welcome to the Hospital Vending Machine program *****")
    print('**********************-----------**************************')
    print()
    print("Here are your department list!")
    for item, selection in vending_machine.items():
        item_list.append((item, selection))

    while switch == 1:
        for i in item_list:
            print(i[0] + ' - [ ' + i[1]+' ]')
        print()
        schedule.run_pending()
        selected_department = input(
            "Enter the Department code number: ").upper()
        if selected_department in vending_machine.values():

            user_switch = 1
            while user_switch == 1:
                for code, doctor_name in doctor_list[selected_department].items():
                    print(doctor_name+' ['+code+']')
                selected_doctor = input("Enter the Doctor code: ").upper()
                if selected_doctor in doctor_list[selected_department].keys():
                    print('Selected Doctor: ',
                          doctor_list[selected_department][selected_doctor])
                    print()

                    print('Your Token Number is:  ** ' + selected_department +
                          '-'+selected_doctor+'-'+str(token_number)+' **')
                    print()
                    switch_doctor = 1
                    while switch_doctor == 1:
                        change_doctor = input(
                            "Do you want to change the doctor? (y/n): ").lower()
                        if change_doctor == "n":
                            user_switch = 0
                            switch_doctor = 0
                            switch = 1
                            update_token()
                        elif change_doctor == "y":
                            user_switch = 1
                            switch_doctor = 0
                        elif change_doctor == "next":
                            call_next_patient()
                            # user_switch = 0
                            # switch_doctor = 0
                            # switch = 1
                            print()
                        else:
                            print()
                            print("Invalid command")
                            print()
                            switch_doctor = 1
                elif selected_doctor == "NEXT":
                    call_next_patient()
                    user_switch = 1
                    print()

                else:
                    print()
                    print("^^^^^^^^Invalid Doctor Code^^^^^^^^")
                    print()
        elif selected_department == "NEXT":
            call_next_patient()
            switch = 1
            print()
        else:
            print()
            print("^^^^^^^^Invalid Department Code^^^^^^^^")
            print()


main()
