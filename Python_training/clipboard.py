import shelve, pyperclip, sys

Shelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    Shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(Shelf.keys())))
    elif sys.argv[1] in Shelf:
        pyperclip.copy(Shelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete' and len(sys.argv) == 3:
        key = sys.argv[2]
        if key in Shelf:
            del Shelf[key]
        else:
            print("Key is not found")
    elif sys.argv[1].lower() == 'delete all':
        Shelf.clear()


Shelf.close()