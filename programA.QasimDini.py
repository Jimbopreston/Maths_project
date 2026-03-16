# simple memory dictionary
memory = {}

# function to find the address of an array element
def element_address(base, index, size):
    address = base + index * size
    return address

# write a value to memory
def write_value(address, value):
    memory[address] = value

# read a value from memory
def read_value(address):
    if address in memory:
        return memory[address]
    else:
        return None


# example test
base = int(input("Enter base address: "))
index = int(input("Enter index: "))
size = int(input("Enter element size: "))
value = int(input("Enter value to store: "))

addr = element_address(base, index, size)

write_value(addr, value)

print("Calculated address:", addr)
print("Value stored:", read_value(addr))