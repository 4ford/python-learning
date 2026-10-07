greeting_raw = input("Greeting: ")

greeting = greeting_raw.strip().lower()[:5]

if greeting == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
#LESSON LEARNED - THE ORDER OF THE IF STATEMENTS MATTERS. IF YOU PUT THE "H" FIRST. ALSO WITH STRING EDITORS [:5] and .strip().