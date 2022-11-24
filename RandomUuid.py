import uuid

number = range(1000)

def randomUuid(output_File, number):
    with open(output_File, 'w') as uuid_File:
        for i in number:
            i = str(uuid.uuid4())
            uuid_File.write(i + '\n')

output_File = str(input("Please input a file path: "))
randomUuid(output_File, number)


