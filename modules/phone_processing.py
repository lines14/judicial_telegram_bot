async def phone_checker(phone):
    if phone[0] == '7':
        phonelist = []
        for i in phone:
            phonelist.append(i)
        phonelist.insert(0, '+')
        phone = ''.join(phonelist)

        if phone[0] == '+':
            slicer = slice(1, len(phone))
            phone_to_check = phone[slicer]
            for i in phone_to_check:
                if i.isdecimal():
                    continue
                else:
                    return 'fail'
            return phone
        else:
            return 'fail'
    elif phone[0] == '8':
        phonelist = []
        for i in phone:
            phonelist.append(i)
        phonelist.remove('8')
        phonelist.insert(0, '7')
        phonelist.insert(0, '+')
        phone = ''.join(phonelist)

        if phone[0] == '+':
            slicer = slice(1, len(phone))
            phone_to_check = phone[slicer]
            for i in phone_to_check:
                if i.isdecimal():
                    continue
                else:
                    return 'fail'
            return phone
        else:
            return 'fail'
    else:
        if phone[0] == '+':
            slicer = slice(1, len(phone))
            phone_to_check = phone[slicer]
            for i in phone_to_check:
                if i.isdecimal():
                    continue
                else:
                    return 'fail'
            return phone
        else:
            return 'fail'

# import re

# text = "+7 999 888 77 66"

# def detect_phone_number(text):
#     phone_number = re.findall('(?:\+ *)?\d[\d\- ]{7,}\d', text)

#     if phone_number != []:
#         print(phone_number[0])
#     else:
#         print('fail')

# def main():
#     detect_phone_number(text)

# main()