
# apl-source:1
# مثال 415 — ترميز طول التسلسل
# apl-source:2
# Run-length encoding
# apl-source:3
# Demonstrates: ضغط وفك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/415-run-length.apl
# apl-source:6

# apl-source:7
def اضغط(نص_الدخل):
    # apl-source:8
    ناتج = ""
    # apl-source:9
    ي = 0
    # apl-source:10
    while ي < len(نص_الدخل):
        # apl-source:11
        عد = 1
        # apl-source:12
        while ي + عد < len(نص_الدخل) and نص_الدخل[ي + عد] == نص_الدخل[ي]:
            # apl-source:13
            عد = عد + 1
        # apl-source:14
        ناتج = ناتج + str(عد) + نص_الدخل[ي]
        # apl-source:15
        ي = ي + عد
    # apl-source:16
    return ناتج
# apl-source:17

# apl-source:18
def افكك(مكبوس):
    # apl-source:19
    ناتج = ""
    # apl-source:20
    ي = 0
    # apl-source:21
    while ي < len(مكبوس):
        # apl-source:22
        عدد = int(مكبوس[ي])
        # apl-source:23
        حرف = مكبوس[ي + 1]
        # apl-source:24
        for _ in range(عدد):
            # apl-source:25
            ناتج = ناتج + حرف
        # apl-source:26
        ي = ي + 2
    # apl-source:27
    return ناتج
# apl-source:28

# apl-source:29
م = اضغط("aaabbbbcddddd")
# apl-source:30
print("مكبوس:", م)
# apl-source:31
print("مفكوك:", افكك(م))
# apl-source:32
