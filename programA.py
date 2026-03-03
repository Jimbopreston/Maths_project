def decimalToHex():
    pass

def littleEndian():
    pass

def ASCIIMemoryDump():
    pass
    #this is a comment from amy

def ArrayAddressing():
    pass
    #this is a comment from jim

def StackFrame():
    pass

def main():
    while True:
        running = True
        break
    while running:

        print('\n Choose an option:')
        print(' 1 - Convert a decimal into heximal and 16-bit binary')
        print(' 2 - Little-endian pack/unpack (16-bit) + memory write/read')
        print(' 3 - ASCII memory dump + null terminator + length scan')
        print(' 4 - Array addressing + dereference (read/write one element)')
        print(' 5 - Stack frame (simplified bp offsets) + register-style view')
        print(' 0 - Quit')

        op = input('Option:')

        if op == '1':
            decimalToHex()

        elif op == '2':
            pass

        elif op == '3':
            pass

        elif op == '4':
            pass

        elif op == '5':
            pass

        elif op == '0':
            print('Exiting Program.')
            running = False

        else:
            print('Invalid Option. Try again')


  
main()

