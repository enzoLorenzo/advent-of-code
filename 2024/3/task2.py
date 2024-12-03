import re

# Przykładowy tekst
with open('input.txt', 'r') as file:

    summary = 0

    text = file.read()
    result = re.sub(r'don\'t\(\).*?do\(\)', '', text, flags=re.DOTALL)
    cleaned_text = re.sub(r'don\'t\(\).*', '', result, flags=re.DOTALL)

    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
    mul_list = re.findall(mul_pattern, cleaned_text)

    for mul in mul_list:
        numbers_pattern = r'mul\((\d+),(\d+)\)'
        match = re.match(numbers_pattern, mul)
        if match:
            number1 = int(match.group(1))
            number2 = int(match.group(2))
            summary += number1*number2

print("Answer: ", summary)
