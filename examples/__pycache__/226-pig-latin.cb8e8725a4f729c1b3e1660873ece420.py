
# apl-source:1
# مثال 226 — لغة الخنزير اللاتينية
# apl-source:2
# Pig Latin
# apl-source:3
# Demonstrates: معالجة كلمات، المتحركات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/226-pig-latin.apl
# apl-source:6

# apl-source:7
def خنزيرية(كلمة):
    # apl-source:8
    متحركات = "aeiou"
    # apl-source:9
    if كلمة[0] in متحركات:
        # apl-source:10
        return كلمة + "way"
    # apl-source:11
    return كلمة[1:] + كلمة[0] + "ay"
# apl-source:12

# apl-source:13
def حول_جملة(جملة):
    # apl-source:14
    كلمات = جملة.split(" ")
    # apl-source:15
    محولة = [خنزيرية(ك) for ك in كلمات]
    # apl-source:16
    return " ".join(محولة)
# apl-source:17

# apl-source:18
print(حول_جملة("hello world"))
# apl-source:19
print(حول_جملة("apple banana cherry"))
# apl-source:20
