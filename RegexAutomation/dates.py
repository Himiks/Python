import shutil, os, re

Date = re.compile(r"""^(.*?)
    ((0|1)?\d)
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

for file in os.listdir('.'):
    mo = Date.search(file)
    if mo == None:
        continue
    
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)
    
    euro = before + day + '-' + month + '-' + year + after
    
    
    absolute = os.path.abspath('.')
    file = os.path.join(absolute, file)
    euro = os.path.join(absolute, euro) 
    
    print('Renaming "%s" to "%s"...'% (file, euro))
    shutil.move(file, euro)
    
    
    