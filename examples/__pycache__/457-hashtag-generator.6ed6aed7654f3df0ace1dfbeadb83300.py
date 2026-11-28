
# apl-source:1
# مثال 457 — مولد هاشتاجات
# apl-source:2
# Hashtag generator
# apl-source:3
# Demonstrates: دمج كلمات بحالة الجمل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/457-hashtag-generator.apl
# apl-source:6

# apl-source:7
def هاشتاج(عبارة):
    # apl-source:8
    ناتج = "#"
    # apl-source:9
    for كلمة in عبارة.split(" "):
        # apl-source:10
        if len(كلمة) > 0:
            # apl-source:11
            ناتج = ناتج + كلمة[0].upper() + كلمة[1:]
    # apl-source:12
    return ناتج
# apl-source:13

# apl-source:14
print(هاشتاج("arabic programming language"))
# apl-source:15
print(هاشتاج("open source community"))
# apl-source:16
