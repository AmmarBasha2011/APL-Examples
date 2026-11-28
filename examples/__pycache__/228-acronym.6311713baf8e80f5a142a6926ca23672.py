
# apl-source:1
# مثال 228 — توليد الاختصارات
# apl-source:2
# Acronym generator
# apl-source:3
# Demonstrates: أول حرف من كل كلمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/228-acronym.apl
# apl-source:6

# apl-source:7
def اختصار(عبارة):
    # apl-source:8
    حروف = []
    # apl-source:9
    for كلمة in عبارة.split(" "):
        # apl-source:10
        if len(كلمة) > 0:
            # apl-source:11
            حروف.append(كلمة[0])
    # apl-source:12
    return "".join(حروف).upper()
# apl-source:13

# apl-source:14
print("as soon as possible ->", اختصار("as soon as possible"))
# apl-source:15
print("for your information ->", اختصار("for your information"))
# apl-source:16
print("arabic programming language ->", اختصار("arabic programming language"))
# apl-source:17
