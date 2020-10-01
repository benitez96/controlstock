import os
import re


def buscar_imgs(directorio):
    png_regex = re.compile(r'.*\.png$')
    for root, folder, names in os.walk(directorio):
        for file in names:
            if png_regex.match(file):
                print(os.path.join(root, file))

            
def main(directorio):
    if len(directorio)> 2:
        raise SystemExit('Solo debe ingresar un directorio.')
    else:
        buscar_imgs(directorio)    
    
    
if __name__ == '__main__':
    import sys
    buscar_imgs(sys.argv[1])