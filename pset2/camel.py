def main():
    sentence = input("camel case: ")
    print("snake case: " + snake_case(sentence))


def snake_case(sentence):
    result = ""
    for c in sentence:
        if c.isupper():
            new_char = "_" + c.lower()
        else:
            new_char = c
        result += new_char
    return result


main()

#Used defmain when I didnt have to. That's a win.