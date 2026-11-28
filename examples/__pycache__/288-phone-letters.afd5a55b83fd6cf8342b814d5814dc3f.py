
# apl-source:1
# مثال 288 — حروف لوحة الهاتف
# apl-source:2
# Phone keypad letter combinations
# apl-source:3
# Demonstrates: تراجع على خريطة أرقام-حروف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/288-phone-letters.apl
# apl-source:6

# apl-source:7
خريطة = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
# apl-source:8

# apl-source:9
def ولد(أرقام, مؤشر, حالية, نتيجة):
    # apl-source:10
    if مؤشر == len(أرقام):
        # apl-source:11
        نتيجة.append(حالية)
        # apl-source:12
        return
    # apl-source:13
    for حرف in خريطة[أرقام[مؤشر]]:
        # apl-source:14
        ولد(أرقام, مؤشر + 1, حالية + حرف, نتيجة)
# apl-source:15

# apl-source:16
def تركيبات(أرقام):
    # apl-source:17
    if len(أرقام) == 0:
        # apl-source:18
        return []
    # apl-source:19
    نتيجة = []
    # apl-source:20
    ولد(أرقام, 0, "", نتيجة)
    # apl-source:21
    return نتيجة
# apl-source:22

# apl-source:23
print(تركيبات("23"))
# apl-source:24
print("عدد تركيبات 234:", len(تركيبات("234")))
# apl-source:25
