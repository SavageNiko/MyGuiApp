file = open('essay.txt', 'r')
content = file.read()
print(content.title())
file.close()

file = open('essay.txt', 'r')
content = file.read()
print(len(content))
file.close()

user_input = input('Add a new member: ')

file = open('members.txt', 'r')
existing_members = file.readlines()
file.close()

existing_members.append(user_input + '\n')

file = open('members.txt', 'w')
existing_members = file.writelines(existing_members)
file.close()

filenames = ['a.txt', 'b.txt', 'c.txt']

for file in filenames:
    file = open(f'{file}', 'r')
    content = file.read()
    print(content)