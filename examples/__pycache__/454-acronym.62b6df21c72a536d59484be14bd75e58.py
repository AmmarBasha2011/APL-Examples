
# apl-source:1
# مثال 454 — مولد الاختصارات
# apl-source:2
# Acronym maker
# apl-source:3
# Demonstrates: أول حرف من كل كلمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/454-acronym.apl
# apl-source:6

# apl-source:7
def اختصار(عبارة):
    # apl-source:8
    ناتج = ""
    # apl-source:9
    for كلمة in عبارة.split(" "):
        # apl-source:10
        if len(كلمة) > 0:
            # apl-source:11
            ناتج = ناتج + كلمة[0].upper()
    # apl-source:12
    return ناتج
# apl-source:13

# apl-source:14
print(اختصار("as soon as possible"))
# apl-source:15
print(اختصار("for your information"))
# apl-source:16
