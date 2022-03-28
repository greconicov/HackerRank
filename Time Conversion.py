# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def timeConversion(s):
    if 'PM' in s:
        if s[:2] != "12":
            prepm = int(s[0:2]) + 12
            hourpm = str(prepm) + str(s[2:-2])
            return hourpm
        else:
            return (s[:-2])

    else:
        if "12" not in s[0:2]:
            return s[:-2]
        else:
            prefixAM= "00"
            return prefixAM + s[2:-2]

print(timeConversion("06:40:03AM"))
print(timeConversion("12:40:22AM"))
print(timeConversion("06:12:22AM"))
