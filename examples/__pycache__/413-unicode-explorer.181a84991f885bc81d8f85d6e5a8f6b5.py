
# apl-source:1
# مثال 413 — مستكشف يونيكود
# apl-source:2
# Unicode explorer
# apl-source:3
# Demonstrates: ترميز_حرف وفك_ترميز_حرف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/413-unicode-explorer.apl
# apl-source:6

# apl-source:7
print("الأبجدية العربية الأولى:")
# apl-source:8
for ي in range(0, 10):
    # apl-source:9
    رمز = 0x0627 + ي
    # apl-source:10
    print(str(رمز) + " = " + chr(رمز))
# apl-source:11

# apl-source:12
print("رموز خاصة:")
# apl-source:13
for رمز in [0x2764, 0x2713, 0x2605]:
    # apl-source:14
    print(chr(رمز))
# apl-source:15

# apl-source:16
print("ترميز حرف أ:", ord("أ"))
# apl-source:17
