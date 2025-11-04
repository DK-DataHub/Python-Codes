contacts = ("Deepak", "Kumar", "Mano", "Ravi", "Dhilip", "Ravi", "Kumar")
contact_list = contacts
print("Contact lists are:",contact_list)
contact_set = set(contacts)
print("Set of unique contacts are:",contact_set)
contact_dict = {
    "Deepak": "4477",
    "Kumar": "6654",
    "Mano": "2312",
    "Ravi": "9989",
    "Dhilip": "7777"
    
}
print("Contact Dictionary:",contact_dict)
print("Is Mano in contact list?","Mano" in contact_list)
print("Dhilip's phone number", contact_dict["Dhilip"])
