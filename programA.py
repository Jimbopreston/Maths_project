def decimalToHex(n):
    
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

def littleEndian(n,addr):

    if not (0 <= n <= 65535):
        print("Input must be between 0 and 65535")
        return
    
    if addr[:2] == '0x':
        addr = int(addr[2:])
    else:
        addr = int(addr)

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
    print(f"UNPACKED {hex_lsb}, {hex_msb} =", n)
    print(f"MEM[0x{addr}] = 0x{hex_lsb}")
    print(f"MEM[0x{addr+1}] = 0x{hex_msb}")
    print(f"READ MEM[0x{addr}] = 0x{hex_lsb}")
    print(f"READ MEM[0x{addr+1}] = 0x{hex_msb}")


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


def write_value(address, value, size):

    if size == 1:
        memory[address] = value & 0xFF

    elif size == 2:
        lsb = value & 0xFF
        msb = (value >> 8) & 0xFF

        memory[address] = lsb
        memory[address + 1] = msb


def read_value(address, size):

    if size == 1:
        return memory.get(address, 0)

    elif size == 2:
        lsb = memory.get(address, 0)
        msb = memory.get(address + 1, 0)

        return (msb << 8) | lsb


def ArrayAddressing():

    base = int(input("Enter base address: "), 0)
    index = int(input("Enter index: "))
    size = int(input("Enter element size (1 or 2): "))
    mode = input("Mode (read/write): ").lower()

    address = element_address(base, index, size)

    print(f"ADDRESS = base + index*size = {hex(address)}")

    if mode == "write":
        value = int(input("Enter value: "))
        write_value(address, value, size)

        print(f"WRITE size={size} value={value} to ADDRESS {hex(address)}")

    elif mode == "read":
        value = read_value(address, size)

        print(f"READ size={size} from ADDRESS {hex(address)} = {value}")

def StackFrame(a , b):
    print('\nSTACK FRAME VIEW')
    print('bp         : RETURN')
    print('bp + 2     : a = ' , a)

def main(): 
    running = True
        
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
            n = int(input("Enter a decimal number (0-65535): "))
            decimalToHex(n)

        elif op == '2':
            n = int(input("Enter a decimal number (0-65535): "))
            addr = int(input("Enter the address to store the integer: "))
            littleEndian(n,addr)

        elif op == '3':
            input_string = input("\nEnter a string (max 10 characters): ")
            ASCIIMemoryDump(input_string)

        elif op == '4':
            
            print("\nARRAY ADDRESSING + MEMORY WRITE/READ")

            base = int(input("Enter base address: "), 0)
            index = int(input("Enter index: "))
            size = int(input("Enter element size (1 or 2): "))
            mode = input("Mode (read/write): ").lower()

            addr = element_address(base, index, size)


            if mode == "write":
                value = int(input("Enter value: "))
                write_value(addr, value, size)

                print(f"\nADDRESS = base + index*size = {hex(addr)}")
                print(f"WRITE size={size} value={value} to ADDRESS {hex(addr)}")

            elif mode == "read":
                value = read_value(addr, size)

                print(f"\nADDRESS = base + index*size = {hex(addr)}")
                print(f"READ size={size} from ADDRESS {hex(addr)} = {value}")

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


  
if __name__ == "__main__":
    main()

