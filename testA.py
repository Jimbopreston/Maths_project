import unittest
from io import StringIO
import sys

from programA import (
    decimalToHex,
    littleEndian,
    ASCIIMemoryDump,
    element_address,
    write_value,
    read_value,
    StackFrame
)


class TestProgramA(unittest.TestCase):

    # helper function to capture printed output
    def capture_output(self, func, *args):
        captured = StringIO()
        sys.stdout = captured
        func(*args)
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    # ------------------------
    # PACK / UNPACK BOUNDARIES
    # ------------------------

    def test_pack_zero(self):
        output = self.capture_output(littleEndian, 0, "1000")
        self.assertIn("LOW BYTE", output)

    def test_pack_one(self):
        output = self.capture_output(littleEndian, 1, "1000")
        self.assertIn("1", output)

    def test_pack_255(self):
        output = self.capture_output(littleEndian, 255, "1000")
        self.assertIn("255", output)

    def test_pack_256(self):
        output = self.capture_output(littleEndian, 256, "1000")
        self.assertIn("256", output)

    def test_pack_65535(self):
        output = self.capture_output(littleEndian, 65535, "1000")
        self.assertIn("65535", output)

    # ------------------------
    # ASCII MEMORY DUMP
    # ------------------------

    def test_ascii_dump_A(self):
        output = self.capture_output(ASCIIMemoryDump, "A")
        self.assertIn("0x41", output)  # ASCII for A
        self.assertIn("LENGTH", output)

    def test_ascii_dump_hello(self):
        output = self.capture_output(ASCIIMemoryDump, "HELLO")
        self.assertIn("0x48", output)  # H
        self.assertIn("0x4F", output)  # O

    # ------------------------
    # ARRAY ADDRESSING
    # ------------------------

    def test_array_address_calculation(self):
        addr = element_address(1000, 3, 2)
        self.assertEqual(addr, 1006)

    # ------------------------
    # STACK FRAME
    # ------------------------

    def test_stack_frame_output(self):
        output = self.capture_output(StackFrame, 5, 7)
        self.assertIn("bp", output)
        self.assertIn("a =", output)

    # ------------------------
    # BINARY LENGTH TEST
    # ------------------------

    def test_binary_is_16_bits(self):
        output = self.capture_output(decimalToHex, 5)
        self.assertIn("0000000000000101", output)

    # ------------------------
    # SIGNED 16 BIT TESTS
    # ------------------------

    def test_signed_65535(self):
        output = self.capture_output(decimalToHex, 65535)
        self.assertIn("-1", output)

    def test_signed_32768(self):
        output = self.capture_output(decimalToHex, 32768)
        self.assertIn("-32768", output)

    # ------------------------
    # MEMORY WRITE / READ
    # ------------------------

    def test_memory_write_read(self):
        write_value(2000, 500, 2)
        value = read_value(2000, 2)
        self.assertEqual(value, 500)


if __name__ == "__main__":
    unittest.main()