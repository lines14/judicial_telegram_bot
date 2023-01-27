phone = '+79998887766'

if phone[0] == '+':
    slicer = slice(1, len(phone))
    phone_to_check = phone[slicer]
    for i in phone_to_check:
        if i.isdecimal():
            continue
        else:
            print('fail')
else:
    print('fail')