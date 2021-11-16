from collections import OrderedDict

input = "eeeeeiiioooooooooouuu"


def run_lenght(input):
    dict = OrderedDict.fromkeys(input, 0)
    for character in input:
        dict[character] += 1
    output = ""
    for character, value in dict.items():
        output += character + str(value)
    return output


print(run_lenght(input))
