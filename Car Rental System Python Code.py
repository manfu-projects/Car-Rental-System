import json

employees = {
    "Workers": [
        {
            "Name": "Max",
            "Age": "26",
            "Password": "X123$%",
            "Role": "Manager",
            "Staff ID": "A101",
            "Date of Register": "23/01/2023",
            "Status": "Active"
        },
        {
            "Name": "Bob",
            "Age": "23",
            "Password": "R456%$",
            "Role": "Customer Service Staff 1",
            "Staff ID": "B101",
            "Date of Register": "13/03/2023",
            "Status": "Active"
        },
        {
            "Name": "Lex",
            "Age": "27",
            "Password": "Y789#$",
            "Role": "Customer Service Staff 2",
            "Staff ID": "B102",
            "Date of Register": "17/05/2023",
            "Status": "Active"
        },
        {
            "Name": "Blake",
            "Age": "24",
            "Password": "L105@#",
            "Role": "Car Service Staff 1",
            "Staff ID": "C101",
            "Date of Register": "08/04/2023",
            "Status": "Active"
        },
        {
            "Name": "Light",
            "Age": "25",
            "Password": "T150$$",
            "Role": "Car Service Staff 2",
            "Staff ID": "C102",
            "Date of Register": "20/03/2023",
            "Status": "Active"
        }
    ]
}

customer = {
    "Customers": [
        {
            "Customer ID": "C100001",
            "Name": "Alan",
            "NRIC": "980829-60-4732",
            "Passport Number": "PA637485909Y",
            "Car Driving License": "D98744632",
            "Contact Address": "98,Main Street, 35000 Taiping, Perak, Malaysia",
            "Phone Number": "05-68324677",
            "Registration Date": "26-12-2023"
        },
        {
            "Customer ID": "C100002",
            "Name": "Stampy",
            "NRIC": "920825-20-4842",
            "Passport Number": "PA664485909Y",
            "Car Driving License": "D88744632",
            "Contact Address": "78,Main Street, 35000 Taiping, Perak, Malaysia",
            "Phone Number": "03-15324677",
            "Registration Date": "24-10-2023"
        },
        {
            "Customer ID": "C100003",
            "Name": "Dan",
            "NRIC": "020825-13-4992",
            "Passport Number": "PA664805909Y",
            "Car Driving License": "D88754632",
            "Contact Address": "65,Main Street, 35000 Taiping, Perak, Malaysia",
            "Phone Number": "04-15324677",
            "Registration Date": "16-03-2024"
        }
    ]
}

car_record = {
    "New Cars": [
        {
            "Car Registration Number": "WPE6038",
            "Car Manufacturer": "PROTON",
            "Car Model": "X70",
            "Year of Manufacturer": "2015",
            "Seating Capacity": 5,
            "Last Service Date": "28-12-2023",
            "Insurance Policy Number": "XB677891",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Renting Rate": "200.00"
        }
    ],
    "Car Rental Transactions": [
        {
            "Registration Number": "KV1234E",
            "Customer ID": "C100001",
            "Rental Date": "15-03-2024",
            "Return Date": "20-03-2024",
            "Rental Period": 6,
            "Total Rental": "1200.00",
            "Brand": "TOYOTA",
            "Model": "CAMRY",
            "Seating Capacity": 5,
            "Rental Availability": "Rented"
        },
        {
            "Registration Number": "KV1112H",
            "Customer ID": "C100002",
            "Rental Date": "09-03-2024",
            "Return Date": "12-03-2024",
            "Rental Period": 4,
            "Total Rental": "1200.00",
            "Brand": "FORD",
            "Model": "EVEREST",
            "Seating Capacity": 7,
            "Rental Availability": "Rented"
        }
    ],
    "Car List": [
        {
            "Registration Number": "KA1331H",
            "Rental Price": "500.00",
            "Brand": "HYUNDAI",
            "Model": "STARIA",
            "Seating Capacity": 10,
            "Insurance Policy Number": "WB100000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Available"
        },
        {
            "Registration Number": "KV1112H",
            "Rental Price": "300.00",
            "Brand": "FORD",
            "Model": "EVEREST",
            "Seating Capacity": 7,
            "Insurance Policy Number": "WA120000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Rented"
        },
        {
            "Registration Number": "WPE6038",
            "Rental Price": "200.00",
            "Brand": "PROTON",
            "Model": "X70",
            "Seating Capacity": 5,
            "Insurance Policy Number": "XB677891",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Available"
        },
        {
            "Registration Number": "KV1234E",
            "Rental Price": "200.00",
            "Brand": "TOYOTA",
            "Model": "CAMRY",
            "Seating Capacity": 5,
            "Insurance Policy Number": "WB130000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Rented"
        },
        {
            "Registration Number": "XYZ3456",
            "Rental Price": "400.00",
            "Brand": "PERODUA",
            "Model": "ALZA",
            "Seating Capacity": 7,
            "Insurance Policy Number": "XA177891",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Available"
        },
        {
            "Registration Number": "KV5678F",
            "Rental Price": "200.00",
            "Brand": "PERODUA",
            "Model": "AXIA",
            "Seating Capacity": 5,
            "Insurance Policy Number": "AY100000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Available"
        },
        {
            "Registration Number": "AB2346Y",
            "Rental Price": "200.00",
            "Brand": "PERODUA",
            "Model": "AXIA",
            "Seating Capacity": 5,
            "Insurance Policy Number": "WY110000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Available"
        },
        {
            "Registration Number": "WP6278F",
            "Rental Price": "300.00",
            "Brand": "PROTON",
            "Model": "X90",
            "Seating Capacity": 7,
            "Insurance Policy Number": "JA200000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Available"
        },
        {
            "Registration Number": "YVA5828",
            "Rental Price": "500.00",
            "Brand": "HYUNDAI",
            "Model": "GRAND STAREX",
            "Seating Capacity": 12,
            "Insurance Policy Number": "PK110000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Available"
        },
        {
            "Registration Number": "KV4178F",
            "Rental Price": "200.00",
            "Brand": "PERODUA",
            "Model": "BEZZA",
            "Seating Capacity": 5,
            "Insurance Policy Number": "PK130000",
            "Insurance Expiry Date": "31-12-2024",
            "Road Tax Expiry Date": "31-12-2024",
            "Rental Availability": "Disposed"
        },
    ]
}


def textfile_reset():
    employees_json = json.dumps(employees, indent=4)
    with open("workers.json", "w") as f1:
        f1.write(employees_json)

    car_record_json = json.dumps(customer, indent=4)
    with open("customer_list.json", "w") as f2:
        f2.write(car_record_json)

    car_record_json = json.dumps(car_record, indent=4)
    with open("car_record.json", "w") as f3:
        f3.write(car_record_json)



def systemLogin():
    with open("workers.json", "r") as f1:
        datas = json.load(f1)

    user_id_attempts = 0

    while user_id_attempts < 3:
        identityCheck = input("__________________________________________"
                              "\nWelcome To Fulin's Car Rental System"
                              "\nAttempt " + str(user_id_attempts + 1) + " - Please Enter Your Staff ID: ")

        user = None

        for worker in datas["Workers"]:
            if worker["Staff ID"] == identityCheck:
                user = worker
                break

        if user:
            pw_attempts = 0
            while pw_attempts < 3:
                pwinput = input("__________________________________________"
                                "\nPlease Enter Your Password: ")
                if "Password" in user and user["Password"] == pwinput and user["Status"] == "Active":
                    print("__________________________________________"
                          "\nYou are logged in as " + user["Role"] + "!")
                    if user["Role"] == "Manager":
                        ManagerChoices()
                        break
                    elif user["Role"] == "Customer Service Staff 1":
                        CSS1choices()
                        break
                    elif user["Role"] == "Customer Service Staff 2":
                        CSS2choices()
                        break
                    elif user["Role"] == "Car Service Staff 1":
                        CarStaff1choices()
                        break
                elif "Password" in user and user["Status"] == "Inactive":
                    print("__________________________________________"
                          "\nYour account has been locked. Contact the manager to reset it.")
                    break
                else:
                    print("__________________________________________"
                          "\nIncorrect password, try again.")
                    pw_attempts += 1
                    if pw_attempts == 3:

                        with open("workers.json", "r") as f1:
                            data = json.load(f1)

                        for worker in data["Workers"]:
                            if worker["Name"] == identityCheck:
                                worker["Status"] = "Inactive"
                                break

                        print("__________________________________________"
                              "\nMaximum login attempts reached. Please ask your manager to reset your status.")

                        with open("workers.json", "w") as f1:
                            json.dump(data, f1, indent=4)

                        return
            break
        else:
            print("__________________________________________"
                  "\nUsername not found, please try again.")
            user_id_attempts += 1

        if user_id_attempts == 3:
            print("__________________________________________"
                  "\nMaximum username attempts reached. Please try again later.")


def ManagerChoices():

    while True:
        choice1 = input("__________________________________________"
                        "\nWhat would you like to do now?"
                        "\n1. Update staff records"
                        "\n2. Register new staff"
                        "\n3. Update own profile"
                        "\n4. View revenue report"
                        "\n5. Remove staff member"
                        "\n6. Change rent rate"
                        "\n7. Log out"
                        "\n")

        if choice1 == '1':

            update_staff_rec = Manager()
            update_staff_rec.update_staff_data()

        elif choice1 == "2":

            register_staff = Manager()
            register_staff.register_staff()

        elif choice1 == "3":

            updater_manager_profile = Manager()
            updater_manager_profile.update_own_profile()

        elif choice1 == "4":

            view_rev = Manager()
            view_rev.view_revenue_report()

        elif choice1 == "5":

            remove_staff = Manager()
            remove_staff.delete_staff()

        elif choice1 == "6":

            remove_staff = Manager()
            remove_staff.change_rent_rate()

        elif choice1 == "7":
            print("__________________________________________"
                  "\nYou have logged out successfully")
            exit()
        else:
            print("__________________________________________"
                  "\nInvalid input. Try again.")


class Manager():

    def update_staff_data(self):

        with open("workers.json", "r") as f1:
            data = json.load(f1)

        staff_id = input("__________________________________________"
                         "\nEnter staff member's ID to access their profile: ")

        user = None

        # Find the user profile
        for worker in data["Workers"]:
            if worker["Staff ID"] == staff_id:
                user = worker
                break

        if staff_id == "A101":
            print("__________________________________________"
                  "\nNot a customer or car service staff member, action unavailable")
            return ()

        if user is None:
            print("__________________________________________"
                  "\nProfile not found. Try again")
            return

        field_to_update = input("__________________________________________"
                                "\nWhich information of the staff member would you like to update? (Type out your "
                                "selection, make sure it matches)"
                                "\n- Name"
                                "\n- Age"
                                "\n- Password"
                                "\n- Role"
                                "\n- Staff ID"
                                "\n- Date of Register"
                                "\n- Status"
                                "\n")

        if field_to_update not in user:
            print("__________________________________________"
                  "\nInvalid field.")
            return

        new_value = input("__________________________________________"
                          f"\nEnter the new value for {field_to_update}: ")

        # Update the user's information
        user[field_to_update] = new_value

        with open("workers.json", "w") as f1:
            json.dump(data, f1, indent=4)

        print("__________________________________________"
              "\nProfile updated successfully.")

    def register_staff(self):

        with open('workers.json', 'r') as f2:
            data = json.load(f2)

        name = input("__________________________________________"
                     "\nEnter the new staff member's name: ")
        age = input("__________________________________________"
                    "\nEnter the new staff member's age (Ex. 22): ")
        password = input("__________________________________________"
                         "\nEnter the new staff member's password (Ex. A100$$): ")
        role = input("__________________________________________"
                     "\nEnter the new staff member's role: ")
        staff_id = input("__________________________________________"
                         "\nEnter the new staff member's Staff ID: ")
        date_of_register = input("__________________________________________"
                                 "\nEnter the date of register (Ex. DD/MM/YYYY): ")
        status = input("__________________________________________"
                       "\nEnter the new staff member's status (Ex. Active/Inactive): ")

        new_staff_data = {
            "Name": name,
            "Age": age,
            "Password": password,
            "Role": role,
            "Staff ID": staff_id,
            "Date of Register": date_of_register,
            "Status": status
        }

        # Add the new staff data to the 'Workers' list
        data['Workers'].append(new_staff_data)

        with open('workers.json', 'w') as f2:
            json.dump(data, f2, indent=4)

        print("__________________________________________"
              "\nNew staff added.")

    def update_own_profile(self):

        with open("workers.json", "r") as f1:
            data = json.load(f1)

        user_name = input("__________________________________________"
                          "\nEnter your staff ID to access your profile: ")

        field_to_update = None

        while True:
            if user_name != "A101":
                break
            elif user_name == "A101":
                field_to_update = input("__________________________________________"
                                        "\nWhich information would you like to update? (Type out your selection"
                                        ", make sure it matches)"
                                        "\n- Name"
                                        "\n- Age"
                                        "\n- Password"
                                        "\n- Role"
                                        "\n- StaffID"
                                        "\n- Date of Register"
                                        "\n- Status"
                                        "\n")
                break

        user = None

        for worker in data["Workers"]:
            if worker["Staff ID"] == user_name:
                user = worker
                break

        if user is None:
            print("__________________________________________"
                  "\nProfile not found. Try again")
            return

        if field_to_update not in user:
            print("__________________________________________"
                  "\nInvalid field.")
            return

        new_value = input("__________________________________________"
                          f"\nEnter the new value for {field_to_update}: ")

        # Update the user's information
        user[field_to_update] = new_value

        with open("workers.json", "w") as f1:
            json.dump(data, f1, indent=4)

        print("__________________________________________"
              "\nProfile updated successfully.")

    def delete_staff(self):

        with open("workers.json", "r") as f1:
            data = json.load(f1)

        user_id = input("__________________________________________"
                        "\nEnter staff member's ID to access their profile: ")

        user_index = None
        for index, worker in enumerate(data["Workers"]):
            if worker["Staff ID"] == user_id:
                user_index = index
                break

        if user_index is not None:
            delete_confirmation = input("__________________________________________"
                                        "\nAre you sure you want to delete this staff member's information? (Yes/No): ")
            if delete_confirmation.lower() == "yes":
                # Delete the worker from the list
                del data["Workers"][user_index]

                # Write the updated data back to the file
                with open("workers.json", "w") as f1:
                    json.dump(data, f1, indent=4)
                print("__________________________________________"
                      f"\nStaff member {user_id} has been deleted.")
            else:
                print("__________________________________________"
                      "\nDeletion cancelled.")
        else:
            print("__________________________________________"
                  "\nStaff member not found.")

    def change_rent_rate(self):

        with open("car_record.json", "r") as f1:
            data = json.load(f1)

        car_registration_number = input("__________________________________________"
                                        "\nEnter car registration number to change rent rate of: ")

        # Flag to check if the car is found
        car_found = False

        for car in data["Car List"]:
            # Checks if the current car's registration number matches the given one
            if car["Registration Number"] == car_registration_number:
                while True:
                    new_rent_rate = input("__________________________________________"
                                          "\nEnter new car renting rate (Ex. 200.00): ")
                    try:
                        # Convert to float and check if it has two decimal places
                        if float(new_rent_rate) and '.' in new_rent_rate and len(new_rent_rate.split('.')[1]) <= 2:
                            car["Rental Price"] = str(new_rent_rate)
                            car_found = True
                            break
                        else:
                            print("__________________________________________"
                                  "\nPlease enter a valid rental price with up to two decimal places.")
                    except ValueError:
                        print("__________________________________________"
                              "\nPlease enter a valid rental price with up to two decimal places.")

        if car_found:
            with open("car_record.json", "w") as file:
                json.dump(data, file, indent=4)
            print("__________________________________________"
                  "\nRent rate successfully updated.")
        else:
            print("__________________________________________"
                  "\nCar not found.")

    def view_revenue_report(self):

        total_revenue = 0

        with open("car_record.json", "r") as file:
            data = json.load(file)

        # Iterate through the car rental transactions and sum up the total rental
        for transaction in data["Car Rental Transactions"]:
            total_revenue += float(transaction["Total Rental"])

        print("__________________________________________"
              f"\nThe total earnings from car rentals is: RM{total_revenue:.2f}")


def CSS1choices():

    while True:
        choice1 = input("__________________________________________"
                        "\nWhat would you like to do now?"
                        "\n1. Update customer records"
                        "\n2. Register new customers"
                        "\n3. View registered customer list"
                        "\n4. Delete customer"
                        "\n5. Log out"
                        "\n")

        if choice1 == '1':

            update_customer_rec = Customer_Service_Staff_1()
            update_customer_rec.update_customer_details()

        elif choice1 == "2":

            register_staff = Customer_Service_Staff_1()
            register_staff.register_customer()

        elif choice1 == "3":

            remove_staff = Customer_Service_Staff_1()
            remove_staff.view_customer_list()

        elif choice1 == "4":

            remove_staff = Customer_Service_Staff_1()
            remove_staff.delete_customer()

        elif choice1 == "5":
            print("__________________________________________"
                  "\nYou have logged out successfully")
            exit()
        else:
            print("__________________________________________"
                  "\nInvalid input. Try again.")


class Customer_Service_Staff_1():

    def register_customer(self):

        with open('customer_list.json', 'r') as customers:
            data2 = json.load(customers)

        customer_ID = input("__________________________________________"
                            "\nEnter the new customer ID (Ex. C100001): ")
        customer_name = input("__________________________________________"
                              "\nEnter the new customer name: ")
        ic_number = input("__________________________________________"
                          "\nEnter the new customer NRIC (Ex. 999999-99-9999): ")
        passport = input("__________________________________________"
                         "\nEnter the new customer;s passport number (Ex. PA1243576890Y): ")
        car_license = input("__________________________________________"
                            "\nEnter the new customer's car driving license (Ex. D12345678): ")
        contact_address = input("__________________________________________"
                                "\nEnter the new customer's contact address (Ex. 10, Main Street, 34000 Taiping, Perak,"
                                " Malaysia): ")
        phone_number = input("__________________________________________"
                             "\nEnter the new customer's phone number (Ex. 03-6478930): ")
        registration_date = input("__________________________________________"
                                  "\nEnter the new customer's registration date (DD-MM-YYYY): ")

        new_customer_data = {
            "Customer ID": customer_ID,
            "Name": customer_name,
            "NRIC": ic_number,
            "Passport Number": passport,
            "Car Driving License": car_license,
            "Contact Address": contact_address,
            "Phone Number": phone_number,
            "Registration Date": registration_date
        }

        data2['Customers'].append(new_customer_data)

        with open('customer_list.json', 'w') as customers:
            json.dump(data2, customers, indent=4)

        print("__________________________________________"
              "\nNew customer added.")

    def update_customer_details(self):

        with open("customer_list.json", "r") as customers:
            data2 = json.load(customers)

        customer_id = input("__________________________________________"
                            "\nEnter customer's ID to access their profile: ")

        customer = None

        for customers2 in data2["Customers"]:
            if customers2["Customer ID"] == customer_id:
                customer = customers2
                break

        if customer is None:
            print("__________________________________________"
                  "\nProfile not found. Try again")
            return

        updatable_fields = ["Phone Number", "NRIC", "Passport Number"]

        field_to_update = input("__________________________________________"
                                "\nWhich information would you like to update? (Phone Number, NRIC or "
                                "Passport Number) ")

        if field_to_update not in updatable_fields:
            print("__________________________________________"
                  "\nInvalid input, you can only update Phone Number, IC Number, or Passport Number.")
            return

        new_value = input("__________________________________________"
                          f"\nEnter the new value for {field_to_update}: ")

        customer[field_to_update] = new_value

        with open("customer_list.json", "w") as customers:
            json.dump(data2, customers, indent=4)

        print("__________________________________________"
              f"\n{field_to_update} has been updated to {new_value} for {customer_id}.")

    def view_customer_list(self):

        with open("customer_list.json", "r") as customers:
            data2 = json.load(customers)

        for customers2 in data2["Customers"]:
            customerNames = customers2["Name"]
            print("__________________________________________"
                  "\nCustomer Name:", customerNames, "|  Customer ID:", customers2["Customer ID"])

    def delete_customer(self):

        with open("customer_list.json", "r") as customers:
            data2 = json.load(customers)

        customer_id = input("__________________________________________"
                            "\nEnter customer's ID to access their profile: ")

        customer_index = None
        for index, customers2 in enumerate(data2["Customers"]):
            if customers2["Customer ID"] == customer_id:
                customer_index = index
                break

        if customer_index is not None:
            delete_confirmation = input("__________________________________________"
                                        "\nAre you sure you want to delete this customer's information? (Yes/No): ")
            if delete_confirmation.lower() == "yes":
                del data2["Customers"][customer_index]

                with open("customer_list.json", "w") as customers:
                    json.dump(data2, customers, indent=4)
                print("__________________________________________"
                      f"\nCustomer {customer_id} has been deleted.")
            else:
                print("__________________________________________"
                      "\nDeletion cancelled.")
        else:
            print("__________________________________________"
                  "\nCustomer not found.")

def CSS2choices():

    while True:
        choice1 = input("__________________________________________"
                        "\nWhat would you like to do now?"
                        "\n1. Check cars availability"
                        "\n2. Record rental details"
                        "\n3. View rental transactions by rental date"
                        "\n4. Reserve car"
                        "\n5. Cancel reservation"
                        "\n6. Delete cancelled transaction"
                        "\n7. Log Out"
                        "\n")

        if choice1 == '1':

            check_cars = Customer_Service_Staff_2()
            check_cars.check_car_availability()

        elif choice1 == "2":

            record_details = Customer_Service_Staff_2()
            record_details.record_rental_details()

        elif choice1 == "3":

            view_transactions = Customer_Service_Staff_2()
            view_transactions.view_rental_transactions()

        elif choice1 == "4":

            reserves = Customer_Service_Staff_2()
            reserves.reserve_car()

        elif choice1 == "5":

            cancel_reserves = Customer_Service_Staff_2()
            cancel_reserves.cancel_reservation()

        elif choice1 == "6":

            cancellation = Customer_Service_Staff_2()
            cancellation.delete_cancelled_transaction()

        elif choice1 == "7":
            print("__________________________________________"
                  "\nYou have logged out successfully")
            exit()
        else:
            print("__________________________________________"
                  "\nInvalid input. Try again.")

class Customer_Service_Staff_2():

    def check_car_availability(self):

        with open("car_record.json", "r") as f3:
            data3 = json.load(f3)

        seats = int(input("__________________________________________"
                          "\nEnter seating capacity: "))

        for cars in data3["Car List"]:
            if cars["Rental Availability"] == "Available":
                if seats <= cars["Seating Capacity"]:
                    print("__________________________________________\n"
                          "Car Available: ", cars["Model"], "|  Registration Number: ", cars["Registration Number"])

    def record_rental_details(self):

        with open("car_record.json", "r") as f3:
            data3 = json.load(f3)

        car_registration_number = input("__________________________________________"
                                        "\nEnter car registration number: ")

        for cars in data3["Car List"]:
            if cars["Registration Number"] == car_registration_number:
                if cars["Rental Availability"] == "Available":
                    cars["Rental Availability"] = "Rented"
                    break
        else:
            print("__________________________________________"
                  "\nCar not found.")
            return

        customer_ID = input("__________________________________________"
                            "\nEnter customer ID (Ex. C10000X): ")
        rental_date = input("__________________________________________"
                            "\nEnter rental date (DD--MM-YYYY): ")
        return_date = input("__________________________________________"
                            "\nEnter return date (DD--MM-YYYY): ")
        while True:
            try:
                rental_period = float(input("__________________________________________"
                                            "\nEnter rental period (Ex. 4): "))
                break
            except ValueError:
                print("__________________________________________"
                      "\nPlease enter numbers only for the rental period.")

        for cars in data3["Car List"]:
            if cars["Registration Number"] == car_registration_number:
                rental_price = float(cars["Rental Price"])
                # Calculate total rental automatically
                total_rental = rental_period * rental_price
                break

        brand = input("__________________________________________"
                      "\nEnter brand (Ex. PERODUA): ")
        model = input("__________________________________________"
                      "\nEnter model (Ex. CR-V): ")
        seats = int(input("__________________________________________"
                          "\nEnter seating capacity (Ex. 5): "))

        transactions_data = {
            "Registration Number": car_registration_number,
            "Customer ID": customer_ID,
            "Rental Date": rental_date,
            "Return Date": return_date,
            "Rental Period": int(rental_period),
            "Total Rental": str(total_rental),
            "Brand": brand,
            "Model": model,
            "Seating Capacity": seats,
            "Rental Availability": "Rented"
        }

        data3['Car Rental Transactions'].append(transactions_data)

        update_rentability = Customer_Service_Staff_2()
        update_rentability.update_rental_availability()

        with open('car_record.json', 'w') as f3:
            json.dump(data3, f3, indent=4)

        print("__________________________________________"
              "\nCar transactions completed.")

    def reserve_car(self):

        with open("car_record.json", "r") as f3:
            data3 = json.load(f3)

        car_reservation = input("__________________________________________"
                                "\nEnter car registration number to reserve: ")

        for cars in data3["Car List"]:
            if cars["Registration Number"] == car_reservation:
                if cars["Rental Availability"] == "Available":
                    cars["Rental Availability"] = "Reserved"
                    print("__________________________________________"
                          f"\nCar {car_reservation} has been reserved.")
                    break
                elif cars["Rental Availability"] != "Available":
                    print("__________________________________________"
                          f"\nCar {car_reservation} is not available for reservation.")
                    return
        else:
            print("__________________________________________"
                  "\nCar cannot be found.")
            return

        with open('car_record.json', 'w') as f3:
            json.dump(data3, f3, indent=4)

    def update_rental_availability(self):

        with open("car_record.json", "r") as f3:
            data3 = json.load(f3)

        for cars in data3["Car List"]:
            cars["Rental Availability"] = "Rented"
            break

    def view_rental_transactions(self):

        with open("car_record.json", "r") as f3:
            data3 = json.load(f3)

        rental_date = input("__________________________________________"
                            "\nEnter the rental date of which transaction you want to see (DD-MM-YYYY): ")

        transaction_found = False

        for transaction in data3["Car Rental Transactions"]:
            if transaction["Rental Date"] == rental_date:
                print("__________________________________________")
                print(json.dumps(transaction, indent=4))
                transaction_found = True
                break

        if not transaction_found:
            print("__________________________________________"
                  "\nNo transactions found for the given date.")

    def cancel_reservation(self):

        with open("car_record.json", "r") as f3:
            data3 = json.load(f3)

        cancel_reservation = input("__________________________________________"
                                   "\nEnter registration number of reserved car to return: ")

        for cars in data3["Car List"]:
            if cars["Registration Number"] == cancel_reservation:
                if cars["Rental Availability"].lower() == "reserved":
                    cars["Rental Availability"] = "Available"
                    print("__________________________________________"
                          f"\nCar {cancel_reservation} returned successfully.")
                    break
                else:
                    print("__________________________________________"
                          "\nNo change needed. Car is not reserved.")
                    break

        with open('car_record.json', 'w') as f3:
            json.dump(data3, f3, indent=4)

    def delete_cancelled_transaction(self):

        with open("car_record.json", "r") as f3:
            data3 = json.load(f3)

        car_cancellation = input("__________________________________________"
                                 "\nEnter cancelled car registration number transaction to delete: ")

        for i, transaction in enumerate(data3["Car Rental Transactions"]):
            if transaction["Registration Number"] == car_cancellation:
                if transaction["Rental Availability"] == "Rented":
                    transaction["Rental Availability"] = "Cancelled"
                    print("__________________________________________"
                          f"\nCar {car_cancellation} has been cancelled and removed from rental transactions.")
                    del data3["Car Rental Transactions"][i]
                    break
                else:
                    print("__________________________________________"
                          f"\nCar {car_cancellation} is either still available for reservation or has not been rented out.")
                    return
        else:
            print("__________________________________________"
                  "\nCar transaction cannot be found.")
            return

        for car in data3["Car List"]:
            if car["Registration Number"] == car_cancellation:
                car["Rental Availability"] = "Available"

        with open('car_record.json', 'w') as f3:
            json.dump(data3, f3, indent=4)

def CarStaff1choices():

    while True:
        choice1 = input("__________________________________________"
                        "\nWhat would you like to do now?"
                        "\n1. Register new car"
                        "\n2. Update car details"
                        "\n3. View car list"
                        "\n4. Delete disposed car"
                        "\n5. Log Out"
                        "\n")

        if choice1 == '1':

            register_car = Car_Service_Staff_1()
            register_car.register_new_car()

        elif choice1 == "2":

            update_details = Car_Service_Staff_1()
            update_details.update_car_details()

        elif choice1 == "3":

            view_cars = Car_Service_Staff_1()
            view_cars.view_car_list()

        elif choice1 == "4":

            delete_car = Car_Service_Staff_1()
            delete_car.delete_disposed_car()

        elif choice1 == "5":
            print("__________________________________________"
                  "\nYou have logged out successfully")
            exit()
        else:
            print("__________________________________________"
                  "\nInvalid input. Try again.")

class Car_Service_Staff_1():

    def register_new_car(self):

        with open("car_record.json", "r") as f4:
            data4 = json.load(f4)

        car_registration = input("__________________________________________"
                                 "\nEnter car registration number: ")
        car_manufacturer = input("__________________________________________"
                                 "\nEnter car manufacturer (Ex. PROTON): ")
        car_model = input("__________________________________________"
                          "\nEnter car model: ")
        manufacturer_year = input("__________________________________________"
                                  "\nEnter manufacturer year (Ex. 2015): ")
        seats = int(input("__________________________________________"
                          "\nEnter seating capacity (Ex. 7): "))
        last_service_date = input("__________________________________________"
                                  "\nEnter last service date (DD-MM-YYYY): ")
        insurance_policy_number = input("__________________________________________"
                                        "\nEnter insurance policy number (Ex. XA123456): ")
        insurance_expiry_date = input("__________________________________________"
                                      "\nEnter insurance expiry date (DD-MM-YYYY): ")
        road_tax_expiry_date = input("__________________________________________"
                                     "\nEnter road tax expiry date (DD-MM-YYYY): ")
        rent_rate = input("__________________________________________"
                          "\nEnter renting rate (Ex. 200.00): ")
        rental_availability = input("__________________________________________"
                                    "\nEnter rental availability:")

        new_car_info = {
            "Car Registration Number": car_registration,
            "Car Manufacturer": car_manufacturer,
            "Car Model": car_model,
            "Year of Manufacturer": manufacturer_year,
            "Seating Capacity": seats,
            "Last Service Date": last_service_date,
            "Insurance Policy Number": insurance_policy_number,
            "Insurance Expiry Date": insurance_expiry_date,
            "Road Tax Expiry Date": road_tax_expiry_date,
            "Renting Rate": rent_rate
        }

        car_list = {
            "Registration Number": car_registration,
            "Rental Price": rent_rate,
            "Brand": car_manufacturer,
            "Model": car_model,
            "Seating Capacity": seats,
            "Insurance Policy Number": insurance_policy_number,
            "Insurance Expiry Date": insurance_expiry_date,
            "Road Tax Expiry Date": road_tax_expiry_date,
            "Rental Availability": rental_availability
        }

        data4["New Cars"].append(new_car_info)
        data4["Car List"].append(car_list)

        with open('car_record.json', 'w') as f4:
            json.dump(data4, f4, indent=4)

        print("__________________________________________"
              f"\nNew car {car_registration} has been successfully added to car list.")

    def update_car_details(self):

        with open("car_record.json", "r") as f4:
            data4 = json.load(f4)

        registration_number = input("__________________________________________"
                                    "\nEnter the car registration number to update information of: ")

        # Find the car by registration number
        car_to_update = None
        for car in data4["Car List"]:
            if car["Registration Number"] == registration_number:
                car_to_update = car
                break

        if car_to_update:
            update_choice = input("__________________________________________"
                                  "\nWhich detail would you like to update?"
                                  "\n1. Insurance Policy Number"
                                  "\n2. Insurance Expiry Date"
                                  "\n3. Road Tax Expiry Date"
                                  "\n4. Exit to main menu"
                                  "\n")

            if update_choice == '1':
                car_to_update["Insurance Policy Number"] = input("__________________________________________"
                                                                 "\nEnter new Insurance Policy Number (Ex. XY100000): ")
            elif update_choice == '2':
                car_to_update["Insurance Expiry Date"] = input("__________________________________________"
                                                               "\nEnter new Insurance Expiry Date (Ex. DD-MM-YYYY): ")
            elif update_choice == '3':
                car_to_update["Road Tax Expiry Date"] = input("__________________________________________"
                                                              "\nEnter new Road Tax Expiry Date (Ex. DD-MM-YYYY): ")
            elif update_choice == '4':
                return

            else:
                print("__________________________________________"
                      "\nInvalid choice. Please try again.")

            with open('car_record.json', 'w') as f4:
                json.dump(data4, f4, indent=4)

            print("__________________________________________"
                  f"\nDetails for car {registration_number} have been updated successfully.")
        else:
            print("__________________________________________"
                  "\nCar with the given registration number not found.")

    def view_car_list(self):

        with open("car_record.json", "r") as f4:
            data4 = json.load(f4)

        view_car = input("__________________________________________"
                         "\nSelect from below"
                         "\n1. View all cars"
                         "\n2. View available cars"
                         "\n")

        if view_car == "1":
            for cars in data4["Car List"]:
                print("__________________________________________"
                      "\nCar number:", cars["Registration Number"], "|  Car Model:", cars["Model"])
        elif view_car == "2":
            for cars in data4["Car List"]:
                if cars["Rental Availability"] == "Available":
                    print("__________________________________________"
                          "\nCar available for rent:", cars["Registration Number"], "|  Car Model:", cars["Model"])
        else:
            print("Invalid input. Please try again.")

    def delete_disposed_car(self):

        with open("car_record.json", "r") as file:
            data = json.load(file)

        delete_car = input("__________________________________________"
                           "\nEnter disposed car registration number to remove: ")

        # Iterate through the car list and remove the car if it meets the criteria
        car_list = data["Car List"]
        for car in car_list[:]:
            if car["Rental Availability"] == "Disposed" and car["Registration Number"] == delete_car:
                car_list.remove(car)
                print("__________________________________________"
                      f"\nCar with registration number {delete_car} has been removed.")
                break
        else:
            print("__________________________________________"
                  "\nCar has not yet been disposed. Deletion unavailable.")
            return

        with open("car_record.json", "w") as file:
            json.dump(data, file, indent=4)




systemLogin()
