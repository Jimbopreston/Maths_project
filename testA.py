import unittest
import programA
#this is the test file it will contain 10 tests for programA that validate its behaviour

from io import StringIO
import sys
from main import decimalToHex, littleEndian, ASCIIMemoryDump, element_address, read_value, write_value

class TestTask1(unittest.TestCase):

    def test_decimalToHex_0(self):
        self.assertEqual(decimalToHex(0), (0, '0', '0000000000000000', 0))

    def test_decimalToHex_255(self):
        self.assertEqual(decimalToHex(255), (255, 'FF', '0000000011111111', 255))

    def test_decimalToHex_65535(self):
        self.assertEqual(decimalToHex(65535), (65535, 'FFFF', '1111111111111111', -1))

    def test_littleEndian_lsb(self):
        lsb, msb = littleEndian(1000, 4096)
        self.assertEqual(lsb, 232)

    def test_littleEndian_msb(self):
        lsb, msb = littleEndian(1000, 4096)
        self.assertEqual(msb, 3)

    def test_ASCIIMemoryDump_length(self):
        self.assertEqual(len(ASCIIMemoryDump("ABC")), 4)

    def test_ASCIIMemoryDump_content(self):
        self.assertEqual(ASCIIMemoryDump("A")[0], 0x41)

    def test_array_address(self):
        self.assertEqual(element_address(0x1000, 2, 4), 0x1008)

    def test_write_read(self):
        write_value(0x2000, 500)
        self.assertEqual(read_value(0x2000), 500)

    def test_array_bounds(self):
        addr = element_address(0x1000, 0, 4)
        write_value(addr, 10)
        self.assertEqual(read_value(addr), 10)

if __name__ == '__main__':
    Unittest.main()

def test_stackFrame():
    pass



