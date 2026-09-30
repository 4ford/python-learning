sentence = input("How are you feeling today? ")

def convert():
    emoji_translate = sentence.replace(":)", "🙂").replace(":(", "🙁")
    print(emoji_translate)

convert()

