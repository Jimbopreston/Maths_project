def decimalToHex():
    n = int(input("Enter a decimal number (0-65535): "))
    
    if not (0 <= n <= 65535):
        print("Input must be between 0 and 65535")
        return
    
    hex_value = format(n, "X")

    bin_value = format(n, "016b")

    if n < 32768:
        signed16 = n
    else:
        signed16 = n - 65536

    print(f"Decimal: {n}")
    print(f"Hexadecimal: {hex_value}")
    print(f"16-bit Binary: {bin_value}")
    print(f"Signed 16-bit: {signed16}")

def littleEndian():
    n = int(input("Enter a decimal number (0-65535): "))
    addr = int(input("Enter the address to store the integer: "))

    if not (0 <= n <= 65535):
        print("Input must be between 0 and 65535")
        return

    bin = format(n, "016b")
    bin_lsb = bin[8:]
    bin_msb = bin[:8]
    lsb = int(bin_lsb, 2)
    msb = int(bin_msb, 2)
    hex_lsb = format(lsb, "X")
    hex_msb = format(msb, "X")
    
    print("")
    print(f"LOW BYTE {hex_lsb} =", lsb)
    print(f"HIGH BYTE {hex_msb} =", msb)
    print("UNPACKED =", n)
    print(f"MEM[0x{addr}] = 0x{hex_lsb}")
    print(f"MEM[0x{addr+1:}] = 0x{hex_msb}")
    print(f"READ MEM[0x{addr}] = 0x{hex_lsb}")
    print(f"READ MEM[0x{addr+1}] = 0x{hex_msb}")

# Dini
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
memory = {}

def element_address(base, index, size):
    return base + index * size

def write_value(address, value):
    memory[address] = value

def read_value(address):
    return memory.get(address, None)


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
            littleEndian()

        elif op == '3':
            input_string = input("\nEnter a string (max 10 characters): ")
            ASCIIMemoryDump(input_string)



        elif op == '4':
            print("\nARRAY ADDRESSING + MEMORY WRITE/READ")
            base = int(input("Enter base address: "))
            index = int(input("Enter index: "))
            size = int(input("Enter element size: "))
            value = int(input("Enter value to store: "))

            addr = element_address(base, index, size)
            write_value(addr, value)

            print("Calculated address:", addr)
            print("Value stored:", read_value(addr))


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

