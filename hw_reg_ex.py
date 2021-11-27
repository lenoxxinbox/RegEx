import re
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.DictReader(f, delimiter=",")
    contacts_list = list(rows)

fio_list = []
for cl in contacts_list:
    phone_number = cl['phone']
    phone = re.compile(r"((\+)?7|8)?\s*\(*495-* *\)* *(\d\d\d)-*(\d\d)-*(\d\d) *\(*(доб. )*(\d*)\)*")
    tel = phone.sub(r"+7(495)\3-\4-\5 \6\7", phone_number)
    fio = (cl['lastname'] + " " + cl['firstname'] + " " + cl['surname'] + " ").split()
    fio.append(cl['organization'])
    fio.append(cl['position'])
    fio.append(tel)
    fio.append(cl['email'])
    fio_list.append(fio)
uniqueFio = []
for item in fio_list:
    itemExist = False
    for x in uniqueFio:
        if x[0] == item[0] and x[1] == item[1]:
            itemExist =True
            break
    if not itemExist:
        uniqueFio.append(item)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(uniqueFio)
