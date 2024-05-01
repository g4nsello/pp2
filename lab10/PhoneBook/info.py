import csv
users=[
    ('personName', 'phoneNumber'),
    ['Arsen', '123'],
    ['Alia', '77777']
]
with open(r'C:\Users\ADMIN\OneDrive\Рабочий стол\arsen\lab10\PhoneBook\abc.csv', 'w', newline='') as f:
    writer=csv.writer(f)
    writer.writerows(users)