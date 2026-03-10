def decimalToHex():
    pass

def littleEndian():
    pass

def ASCIIMemoryDump(input_string): 
    input_string = input_string[:10]

    base_address = 0x1000

    for index, character in enumerate(input_string):
        ascii_value = ord(character)
        address = base_address + index
        print(f"0x{address:04X} : 0x{ascii_value:02X}")
        
    null_address = base_address + len(input_string)
    print(f"0x{null_address:04X} : 0x00")

    print(f"LENGTH (until 0x00) = {len(input_string)}")

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
            input_string = input("\nEnter a string (max 10 characters): ")
            ASCIIMemoryDump(input_string)



        elif op == '4':
            pass

        elif op == '5':
            int1 = int(input('\nPlease input integer "a": '))
            int2 = int(input('Please input integer "b": '))
            StackFrame(int1 , int2)
            pass

        elif op == '0':
            print('Exiting Program.')
            running = False

        else:
            print('Invalid Option. Try again')


  
main()

