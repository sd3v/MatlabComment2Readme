import os
import sys 

# going to implement pdf export
# using Markdown2PDF 0.1.4
# https://pypi.org/project/Markdown2PDF/

# pip install Markdown2PDF


def main():
    filename= sys.argv[1].split('.')[0] +".md"
    file=open(sys.argv[1],"r")
    output=open(filename , "w+")
    
    lines=file.readlines()
    
    c=0

    for line in lines:
        if not line.strip():
            continue
        if line[:1] == '%':
            if c == 0:
                output.write(line[1:]+ "  ")
            else:
                c=0
                output.write('```' +'\n')
                output.write(line[1:]+"  ")
        else:
            if c == 0:
                output.write('```Matlab'+'\n')
                output.write(line+ '\n')
                c+=1
            else:
                output.write(line + "  ")

    output.close()
    file.close()

if __name__ == "__main__":
    main()
