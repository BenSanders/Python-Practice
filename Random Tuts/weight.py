weight = int(input("Weight: "))
unit = input("(k)g or (L)bs ")

if unit.upper() == "K":
	converted = weight / 0.45
	print("Weight in Lbs: " + str(converted))
else:
	converted = weight * 0.45
	print("Weight in Kgs: " + str(converted))


# From this video https://youtu.be/kqtD5dpn9C8?t=2376