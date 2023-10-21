mike = int(input('How much cash does Mike have? '))
ivan = int(input('How much cash does Ivan have? '))
invest = int(input('How much money needs to be invested? '))

if mike >= invest and ivan >= invest:
    print(2)
elif mike >= invest and ivan < invest:
    print('Mike')
elif mike < invest and ivan >= invest:
    print('Ivan')
elif mike < invest and ivan < invest and mike + ivan >= invest:
    print(1)
else:
    print(0)