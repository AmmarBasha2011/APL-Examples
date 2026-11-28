
# apl-source:1
# مثال 189 — فحص توازن الأقواس
# apl-source:2
# Balanced brackets check
# apl-source:3
# Demonstrates: المكدس بالقائمة، القواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/189-balanced-brackets.apl
# apl-source:6

# apl-source:7
def متوازن(نص_الدخل):
    # apl-source:8
    مكدس = []
    # apl-source:9
    أزواج = {")": "(", "]": "[", "}": "{"}
    # apl-source:10
    for حرف in نص_الدخل:
        # apl-source:11
        if حرف == "(" or حرف == "[" or حرف == "{":
            # apl-source:12
            مكدس.append(حرف)
        # apl-source:13
        elif حرف == ")" or حرف == "]" or حرف == "}":
            # apl-source:14
            if len(مكدس) == 0:
                # apl-source:15
                return False
            # apl-source:16
            if مكدس.pop() != أزواج[حرف]:
                # apl-source:17
                return False
    # apl-source:18
    return len(مكدس) == 0
# apl-source:19

# apl-source:20
print("()", متوازن("()"))
# apl-source:21
print("([{}])", متوازن("([{}])"))
# apl-source:22
print("(]", متوازن("(]"))
# apl-source:23
print("((", متوازن("(("))
# apl-source:24
