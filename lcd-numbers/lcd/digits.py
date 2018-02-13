class Digit(object):
    def __init__(self, digit, representation):
        self._digit = digit
        self._digit_representation = representation

    def scale(self, scale_factor=1):
        if scale_factor == 1:
            return self
        scaled_lines = []
        for line in self._digit_representation:
            scaled_lines.append(line[0] + line[1]*scale_factor + line[2])

        scaled_digit = []
        scaled_digit.append(scaled_lines[0])
        for _ in xrange(scale_factor):
            scaled_digit.append(scaled_lines[1])
        scaled_digit.append(scaled_lines[2])
        for _ in xrange(scale_factor):
            scaled_digit.append(scaled_lines[3])
        scaled_digit.append(scaled_lines[4])

        return Digit(self._digit, scaled_digit)

    def get_representation(self):
        return self._digit_representation


class Digits(object):
    def __init__(self, digit_representations, scale_factor=1):
        self._digits = [Digit(i, representation).scale(scale_factor)
                        for i, representation in enumerate(digit_representations)]
        self._scale_factor = scale_factor

    def get_digit(self, digit):
        return self._digits[int(digit)] #This is an indexed getter

    def assemble_numbers(self, numbers):
        lcd_number = []
        line_count = 3+2*self._scale_factor
        for index in xrange(line_count):
            lcd_number.append(self._assemble_line(index, numbers))
        return lcd_number

    def _assemble_line(self, index, numbers):
        line = ""
        for number in str(numbers):
            digit = self.get_digit(number)
            line += digit.get_representation()[index]
        return line

    def print_numbers(self, numbers, printer):
        for line in self.assemble_numbers(numbers):
            printer(line)


class DigitReader(object):
    def __init__(self, resource_directory):
        self._resource_directory = resource_directory

    def read_digits(self, scale_factor=1):
        return Digits([self._read_digit_from_file(number) for number in xrange(10)], scale_factor)

    def _read_digit_from_file(self, digit):
        file_name = self._resource_directory + str(digit) + ".txt"
        with open(file_name) as file_handle:
            return [line.replace('\n', '') for line in file_handle.readlines()]
