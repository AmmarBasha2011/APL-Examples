
# apl-source:1
# مثال 224 — شيفرة مورس
# apl-source:2
# Morse code
# apl-source:3
# Demonstrates: قاموس تحويل، بناء نص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/224-morse.apl
# apl-source:6

# apl-source:7
مورس = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", " ": "/"}
# apl-source:8

# apl-source:9
def إلى_مورس(نص_الدخل):
    # apl-source:10
    رموز = []
    # apl-source:11
    for حرف in نص_الدخل.lower():
        # apl-source:12
        if حرف in مورس:
            # apl-source:13
            رموز.append(مورس[حرف])
    # apl-source:14
    return " ".join(رموز)
# apl-source:15

# apl-source:16
def من_مورس(شفرة):
    # apl-source:17
    عكس = {}
    # apl-source:18
    for حرف in مورس:
        # apl-source:19
        عكس[مورس[حرف]] = حرف
    # apl-source:20
    حروف = []
    # apl-source:21
    for رمز in شفرة.split(" "):
        # apl-source:22
        if رمز in عكس:
            # apl-source:23
            حروف.append(عكس[رمز])
    # apl-source:24
    return "".join(حروف)
# apl-source:25

# apl-source:26
شفرة = إلى_مورس("sos apl")
# apl-source:27
print("مورس:", شفرة)
# apl-source:28
print("مفكوكة:", من_مورس(شفرة))
# apl-source:29
