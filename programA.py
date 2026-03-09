def decimalToHex():
    pass

def littleEndian():
    pass

def ASCIIMemoryDump():
    pass
    #input a string with a maximum of 10 characters
    #output one line per stored byte in this form: 0x1000 : 0xHH
    #Rules:
    #Base address is 0x1000
    #Each character is stored at the next address (+1)
    #You must also store a null terminator 0x00 after the last character (like a C-style string) and include it in the dump
    #After the dump, print: LENGTH (until 0x00) = <number>

def ArrayAddressing():
    pass
    

def StackFrame(a , b):
    print('\nSTACK FRAME VIEW')
    print('bp         : RETURN')
    print('bp + 2     : a = ' , a)
    print('bp + 4     : b = ' , b)
    print('\nREGISTER VIEW')
    print('AX = ', a)
    print('BX = ', b)
    print('AX (AX+BX) = ', a + b)

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
            a = int(input('\nPlease input integer "a": '))
            b = int(input('Please input integer "b": '))
            StackFrame(a , b)
            pass

        elif op == '0':
            print('Exiting Program.')
            running = False

        else:
            print('Invalid Option. Try again')


  
main()

