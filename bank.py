greeting = input("greeting:").strip().lower()
if greeting.startswith("hello"):
    print("$")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")