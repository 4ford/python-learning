answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

real_answer = answer.strip().lower()

if real_answer in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")