
# apl-source:1
# مثال 229 — عكس الكلمات والجمل
# apl-source:2
# Word and sentence reverser
# apl-source:3
# Demonstrates: تقطيع عكسي، عكس ترتيب الكلمات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/229-word-reverser.apl
# apl-source:6

# apl-source:7
def اعكس_حروف(كلمة):
    # apl-source:8
    return كلمة[::-1]
# apl-source:9

# apl-source:10
def اعكس_ترتيب(جملة):
    # apl-source:11
    كلمات = جملة.split(" ")
    # apl-source:12
    معكوسة = []
    # apl-source:13
    for ي in range(len(كلمات)):
        # apl-source:14
        معكوسة.append(كلمات[len(كلمات) - 1 - ي])
    # apl-source:15
    return " ".join(معكوسة)
# apl-source:16

# apl-source:17
print(اعكس_حروف("مرحبا"))
# apl-source:18
print(اعكس_حروف("APL"))
# apl-source:19
print(اعكس_ترتيب("البرمجة بالعربية جميلة"))
# apl-source:20
