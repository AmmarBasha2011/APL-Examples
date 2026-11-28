
# apl-source:1
# مثال 414 — شيفرة مورس
# apl-source:2
# Morse code
# apl-source:3
# Demonstrates: قاموس حروف وترميز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/414-morse-code.apl
# apl-source:6

# apl-source:7
مورس = {
    # apl-source:8
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    # apl-source:9
    "S": "...", "O": "---", "L": ".-..", "P": ".--.", "T": "-"
# apl-source:10
}
# apl-source:11

# apl-source:12
def إلى_مورس(نص_الدخل):
    # apl-source:13
    ناتج = []
    # apl-source:14
    for حرف in نص_الدخل:
        # apl-source:15
        if حرف == " ":
            # apl-source:16
            ناتج.append("/")
        # apl-source:17
        elif مورس.get(حرف) != None:
            # apl-source:18
            ناتج.append(مورس[حرف])
    # apl-source:19
    return " ".join(ناتج)
# apl-source:20

# apl-source:21
print(إلى_مورس("SOS"))
# apl-source:22
print(إلى_مورس("APL"))
# apl-source:23
