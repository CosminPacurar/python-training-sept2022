"""
This is an example script
"""

print("hello world")
x = 10
print(x)

text = ("If we have a long logical line, we can split it into physical lines by"
        " using the backslash at the end of the line so that Python understands"
        " that the next physical line should be considered as part of the"
        " current logical line.")
print(text)

# Indentation example with a simple condition
if x > 0:
    print("inside if")
    print("still inside if")

print("outside if")

multiline_str = """
Test
Test2
"""

print(multiline_str)

s = "hello"
if "hel" not in s:
    pass

greeting = "hello world"

if greeting != s:
    pass

# not (operand operator operand)
# operand negated_operator operand

name = 'john'
age = 40
msg = f'My name is {name.capitalize()} and my age next year is {age + 1}.'
print(msg)
