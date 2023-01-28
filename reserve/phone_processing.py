# phone = '+79998887766'
# phone = 'Напишите мне в телеграм'


# if phone == 'Напишите мне в телеграм':
#     pass
# else:
#     if phone[0] == '+':
#         slicer = slice(1, len(phone))
#         phone_to_check = phone[slicer]
#         for i in phone_to_check:
#             if i.isdecimal():
#                 continue
#             else:
#                 print('fail')
#     else:
#         print('fail')


import re

text = "+7 999 888 77 66"

def detect_phone_number(text):
    phone_number = re.findall('(?:\+ *)?\d[\d\- ]{7,}\d', text)

    if phone_number != []:
        print(phone_number[0])
    else:
        print('fail')








def main():
    detect_phone_number(text)

main()