def arrange_and_clean(text):
    lines = [line.strip() for line in text.split("\n")]

    def has_number(line):
        for i, char in enumerate(line):
            if not char.isdigit() and char != ':':
                return line[:i].strip(':')
        return line.strip(':')

    def get_number(line):
        num = has_number(line)
        return int(num) if num else float('inf')  # Use infinity for lines without numbers

    sorted_lines = sorted(lines, key=get_number)

    return "\n".join(line[len(has_number(line)) + 1:].strip() if has_number(line) else line for line in sorted_lines)

# Example usage
text = """:2 hi
:1 bye
:56 ayo man
:1 bye bye
ayo whatsap
:22 you look like shit"""
cleaned_text = arrange_and_clean(text)
print(cleaned_text)