phone=input("Enter Your Phone Number")
digit_map={
    '1':'One',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero',
}

output = ""
for a in phone:
   output+= digit_map.get(a,'!')+ " "
print(output)