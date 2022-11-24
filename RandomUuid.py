import uuid
import datetime


file_Name = str(input("Please input a file path: "))
file_timestamp = datetime.datetime.now().strftime('%d-%m-%Y-%H:%M:%S-')
output_File = file_timestamp + file_Name
number = range(int(input("Enter the number of UUID that you need: ")))

def randomUuid(output_File, number):
    with open(output_File, 'w') as uuid_File:
        for i in number:
            i = str(uuid.uuid4())
            uuid_File.write(i + '\n')


randomUuid(output_File, number)


