def day1_1(input_file_path: str) -> int:
    total = 0
    with open(input_file_path, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            val = ""

            # Iterate forwards
            i = 0
            while line[i].isalpha():
                i += 1
            val += line[i]

            # Iterate backwards
            j = len(line) - 1
            while line[j].isalpha():
                j -= 1
            val += line[j]

            total += int(val)
    return total


test = day1_1("test_input.txt")
print(f"Test result: {test}")
assert test == 142
print(f"Real result: {day1_1('input.txt')}")


def day1_2(input_file_path: str) -> int:
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    spelled_digits = digit_map.keys()
    total = 0
    with open(input_file_path, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            val = ""

            # Iterate forwards
            i = 0
            current_str = ""
            while line[i].isalpha():
                current_str += line[i]
                if any(
                    spelled_digit in current_str for spelled_digit in spelled_digits
                ):
                    break
                i += 1
            # Check if digit
            if not any(
                spelled_digit in current_str for spelled_digit in spelled_digits
            ):
                val += line[i]
            else:  # cur_str contains a spelled digit
                while current_str not in spelled_digits:
                    current_str = current_str[1:]
                val += digit_map[current_str]

            # Iterate backwards
            j = len(line) - 1
            current_str = ""
            while line[j].isalpha():
                current_str = line[j] + current_str
                if any(
                    spelled_digit in current_str for spelled_digit in spelled_digits
                ):
                    break
                j -= 1
            # Check if digit
            if not any(
                spelled_digit in current_str for spelled_digit in spelled_digits
            ):
                val += line[j]
            else:  # cur_str contains a spelled digit
                while current_str not in spelled_digits:
                    current_str = current_str[:-1]
                val += digit_map[current_str]

            total += int(val)
    return total


test = day1_2("test_input2.txt")
print(f"Test result: {test}")
assert test == 281
print(f"Real result: {day1_2('input.txt')}")
