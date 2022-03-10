#At first we have to run pip install phonenumbers in the command prompt
import phonenumbers
from phonenumbers import timezone, geocoder,carrier
number=input("Enter Your Mobile Number with +__: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
carry=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
reg1=geocoder.description_for_valid_number(phone,"en")
print(phone)
print(time)
print(carry)
print(reg)
print(reg1)



