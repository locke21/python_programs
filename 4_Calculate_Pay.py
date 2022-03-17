# --- Assignment for Dr. Chuck's Python Specialization Coursera Course --- #
# --- Code written initially 1-2 weeks into learning Python --- #


def computepay(h, r):
    if h <= 40:
        return h * r
    elif h >= 40:
        overtime = (h - 40) * (r*.5)
        overtimepay = (h * r) + overtime
        return overtimepay


hrs = input("Enter Hours:")
rate = input("Enter Rates:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)

# --- Code Re-Written 3 Months later after finishing Dr. Chuck's Specializtion --- #
# --- Currently on day 48 of Dr. Angela Wu's 100-Days of Code Python Challenge --- #


def computepay(h, r):
    return (float(h) * float(r)) + ((float(h) - 40) * (float(r) * .5)) if float(h) > 40 else float(h) * float(r)


print(computepay(input("Enter Hours:"), input("Enter Rates:")))
