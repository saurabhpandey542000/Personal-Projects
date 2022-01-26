# import the Package "phoneNumbers"
import phonenumbers

# Attached the Second file(test.py) -------> from test.py file We can import the Number that i want to locate -->
from test import number

# Now we Can import geocoder from the phonenumbers package
# ( Geocoder is the Building function in the phonenumber )
from phonenumbers import geocoder


# CH is nothings but  C for country and H for History
ch_number = phonenumbers.parse(number , "CH")

print(geocoder.description_for_number(ch_number , "en"))


# Carrier is used for provide the service provider name -->
from phonenumbers import carrier
service_number =phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))





