'''
dict set list are mutubale items remaining all are immutable

pop popitem 
'''

notes={}

name = input("Enter your name: ")

while True:
    print(f'Hey{name},Welcome to the notes !! ')
    if notes:
        for i in notes:
            print(i.ljust(15,' '),':',notes[i])
        else:
            print("Empty Notes")
        
    print('[A]dd Note')
    print('[E]dit Note')
    print('[D]elet Note')
    print('[B]ack')

    ch = input("Enter your choice: ").upper()
    if ch == 'A':
        note_name = input("Enter the note name: ").title()
        content = input("Write your thoughts.......: ")
        notes[note_name] = content

    elif ch == 'E':
        note_name = input("Enter the note name to edit:").title()
        if note_name in notes:
            new_content = input("Write your thoughts....")
            notes[note_name] += new_content
        else:
            print(f'{note_name} is not available')

    elif ch == 'D':
        note_name = input("Enter the note name to delete: ").title()
        notes.pop(note_name)
        print(f'{note_name}is deleted successfully !!')

    elif ch == 'B':
        print(f'Thank You,{name} !!')
    
        
