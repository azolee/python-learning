with open('./kedvenc_idezetek.txt', 'w') as file:
    file.write('"In order to write code, you read code 10 times more than you write it." by Uncle Bob\n')
    file.write('"The best way to learn is to teach."\n')
    file.write('"The best way to teach is to learn."\n')
    file.write('"The best way to learn is to do."\n')
    file.write('"The best way to do is to learn."\n')

with open('./kedvenc_idezetek.txt', 'r') as file:
    for line in file:
        print(f"{line}", end='')