
# apl-source:1
# مثال 432 — شريط تقدم نصي
# apl-source:2
# Text progress bar
# apl-source:3
# Demonstrates: رسم نسبة مئوية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/432-progress-bar.apl
# apl-source:6

# apl-source:7
def شريط(نسبة):
    # apl-source:8
    ممتلئ = int(نسبة / 10)
    # apl-source:9
    رسم = ""
    # apl-source:10
    for ي in range(10):
        # apl-source:11
        if ي < ممتلئ:
            # apl-source:12
            رسم = رسم + "#"
        # apl-source:13
        else:
            # apl-source:14
            رسم = رسم + "-"
    # apl-source:15
    return "[" + رسم + "] " + str(نسبة) + "%"
# apl-source:16

# apl-source:17
for نسبة in [0, 25, 50, 75, 100]:
    # apl-source:18
    print(شريط(نسبة))
# apl-source:19
