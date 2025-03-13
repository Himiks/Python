# number = int(input("Enter a number for collatz sequence:"))



# def collatz(number):
#     if number % 2 == 0:
#         return number // 2
#     elif number % 2 != 0:
#         return 3 * number + 1
#
#
# while number != 1:
#     number = collatz(number)
#     print(number)


# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames)+1) + '(Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break;
#     catNames = catNames + [name]
# print('The cat names are:')
# for name in catNames:
#     print('' + name)

# for i in range (4):
#     print(i)


# for i in [0, 1, 2, 3]:
#     print(i)

# supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
# for i in range (len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# if 'pen' in supplies:
# if 'pen' not in supplies:

# cat = ['fat', 'black', 'loud']
# size, color, disposition = cat


# def list_to_string(items):
#     if not items:
#         return ''
#     elif len(items) == 1:
#         return items[0]
#     else:
#         return ', '.join(items[:-1]) + ', and' + items[-1]
#
#
# items = ['apples', 'bananas', 'tofu', 'cats']
# print(list_to_string(items))


def draw_picture(grid):
    for i in range(0, 6):
        print('\n')
        for j in range(0, 9):
            print(grid[j][i], end='')

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

draw_picture(grid)
