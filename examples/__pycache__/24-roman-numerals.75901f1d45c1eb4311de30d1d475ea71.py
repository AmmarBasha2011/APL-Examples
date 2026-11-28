
# apl-source:1
# مثال 24 — تحويل إلى أرقام رومانية
# apl-source:2
# Roman Numerals Converter
# apl-source:3
# Demonstrates: dicts, division/modulo, lists, algorithmic thinking
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/24-roman-numerals.apl
# apl-source:6

# apl-source:7
def دالة_إلى_روماني(رقم):
    # apl-source:8
    جدول = [
        # apl-source:9
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        # apl-source:10
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        # apl-source:11
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    # apl-source:12
    ]
    # apl-source:13
    النتيجة = ""
    # apl-source:14
    المتبقي = رقم
    # apl-source:15
    for زوج in جدول:
        # apl-source:16
        القيمة = زوج[0]
        # apl-source:17
        الرمز = زوج[1]
        # apl-source:18
        while المتبقي >= القيمة:
            # apl-source:19
            النتيجة = النتيجة + الرمز
            # apl-source:20
            المتبقي = المتبقي - القيمة
    # apl-source:21
    return النتيجة
# apl-source:22

# apl-source:23
إلى_روماني = دالة_إلى_روماني
print("=== الأرقام الرومانية ===")
# apl-source:24
for رقم in [1, 4, 9, 14, 40, 90, 400, 1990, 2024, 3999]:
    # apl-source:25
    print(f"  {رقم:>5} = {دالة_إلى_روماني(رقم)}")
# apl-source:26
