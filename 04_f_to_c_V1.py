# Quick component to convert degrees F to C
# Dunction take in value, does conversion and puts answer into a list


def to_c(from_f):
    celsius = (from_f * 5/9) - 32
    return celsius


# Main Routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)