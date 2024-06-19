import re

hello22 = 'inquire.mcq(q="you look like a clown?",o=yes,idk,no)'

# Extract the values of q and o using regular expressions
match = re.search(r"inquire\.mcq\(q=(.+?),o=(.+)\)", hello22)
if match:
    q_value = match.group(1)
    o_values = [value.strip() for value in match.group(2).split(",")]
    print("q:", q_value)
    print("o:", o_values)
else:
    print("No match found")