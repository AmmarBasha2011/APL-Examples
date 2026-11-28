
# apl-source:1
# مثال 298 — تحويل متعرج
# apl-source:2
# Zigzag conversion
# apl-source:3
# Demonstrates: توزيع على صفوف ثم قراءة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/298-zigzag.apl
# apl-source:6

# apl-source:7
def متعرج(نص_الدخل, صفوف):
    # apl-source:8
    if صفوف == 1:
        # apl-source:9
        return نص_الدخل
    # apl-source:10
    أسطر = []
    # apl-source:11
    for _ in range(صفوف):
        # apl-source:12
        أسطر.append("")
    # apl-source:13
    سطر = 0
    # apl-source:14
    اتجاه = 1
    # apl-source:15
    for حرف in نص_الدخل:
        # apl-source:16
        أسطر[سطر] = أسطر[سطر] + حرف
        # apl-source:17
        if سطر == 0:
            # apl-source:18
            اتجاه = 1
        # apl-source:19
        elif سطر == صفوف - 1:
            # apl-source:20
            اتجاه = -1
        # apl-source:21
        سطر = سطر + اتجاه
    # apl-source:22
    return "".join(أسطر)
# apl-source:23

# apl-source:24
print(متعرج("PAYPALISHIRING", 3))
# apl-source:25
print(متعرج("AB", 1))
# apl-source:26
