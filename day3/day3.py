def day3(input_file_path: str) -> int:
    total = 0
    with open(input_file_path, "r") as file:
        lines = file.readlines()
        number_of_lines = len(lines)
        # Iterate through all lines of file
        for line_index, line in enumerate(lines):
            line = line.rstrip("\n")
            prev_line = None
            next_line = None
            if line_index > 0:
                prev_line = lines[line_index - 1]
            if line_index < number_of_lines - 1:
                next_line = lines[line_index + 1]
            # Iterate through all characters in line
            j = 0
            line_length = len(line)
            while j < line_length:
                char = line[j]
                if char.isdigit():
                    valid_part = False
                    num = ""
                    num_indices = []
                    # Build out string of digits until you encounter a non-digit
                    num += char
                    # Track indices too
                    num_indices.append(int(j))
                    while j + 1 < line_length and line[j + 1].isdigit():
                        j += 1
                        num += line[j]
                        num_indices.append(j)
                    # Set valid_part to True if any adjacent node (including diagonals) contains symbols
                    for index in num_indices:
                        check_left = True if index - 1 >= 0 else False
                        check_right = True if index + 1 < line_length else False
                        # Check above
                        if prev_line:
                            if is_char_symbol(prev_line[index]):
                                valid_part = True
                                break
                        # Check below
                        if next_line:
                            if is_char_symbol(next_line[index]):
                                valid_part = True
                                break
                        # Check left for all: current line, above, below
                        if check_left:
                            # Check if value on current line is special character
                            if is_char_symbol(line[index - 1]):
                                valid_part = True
                                break
                            # Ensure that prev_line exists before checking
                            if prev_line:
                                if is_char_symbol(prev_line[index - 1]):
                                    valid_part = True
                                    break
                            # Ensure that next_line exists before checking
                            if next_line:
                                if is_char_symbol(next_line[index - 1]):
                                    valid_part = True
                                    break
                        # Check right for all: current line, above, below
                        if check_right:
                            if is_char_symbol(line[index + 1]):
                                valid_part = True
                                break
                            if prev_line:
                                if is_char_symbol(prev_line[index + 1]):
                                    valid_part = True
                                    break
                            if next_line:
                                if is_char_symbol(next_line[index + 1]):
                                    valid_part = True
                                    break
                    # Add part number to total if part is valid
                    if valid_part is True:
                        print(num)
                        total += int(num)
                j += 1
    return total


def is_char_symbol(char: str) -> bool:
    return char != "." and not char.isalnum()


test = day3("test_input.txt")
print(f"Test result: {test}")
assert test == 4361
result = day3("input.txt")
print(f"Real result: {result}")
assert result == 371924
