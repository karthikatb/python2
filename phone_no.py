def is_valid_mobile_number(number):
    if len(number)==10 and number[0] in "987":
        return True
    return False
mobile_number=input("enter a mobile number:")
if is_valid_mobile_number(mobile_number):
    print(f"the mobile number {mobile_number} is valid")
else:
    print(f"the mobile number {mobile_number} is invalid")
