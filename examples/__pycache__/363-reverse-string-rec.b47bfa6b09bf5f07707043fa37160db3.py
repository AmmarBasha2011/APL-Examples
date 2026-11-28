
# apl-source:1
# مثال 363 — عكس نص بالعودية
# apl-source:2
# Recursive string reverse
# apl-source:3
# Demonstrates: تقسيم المشكلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/363-reverse-string-rec.apl
# apl-source:6

# apl-source:7
def اعكس(نص_الدخل):
    # apl-source:8
    if len(نص_الدخل) <= 1:
        # apl-source:9
        return نص_الدخل
    # apl-source:10
    return اعكس(نص_الدخل[1:]) + نص_الدخل[0]
# apl-source:11

# apl-source:12
print(اعكس("مرحبا"))
# apl-source:13
print(اعكس("APL"))
# apl-source:14
