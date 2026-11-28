
# apl-source:1
# مثال 514 — فرز شل
# apl-source:2
# Shell sort
# apl-source:3
# Demonstrates: فرز بالفجوات، فرز شل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/514-shell-sort.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# فرز شل بفجوات متناقصة
# apl-source:15
ق = [23, 12, 1, 8, 34, 54, 2, 3, 21, 9]
# apl-source:16
ن = len(ق)
# apl-source:17
فجوة = ن // 2
# apl-source:18
while فجوة > 0:
    # apl-source:19
    for i in range(فجوة, ن):
        # apl-source:20
        م = ق[i]
        # apl-source:21
        j = i
        # apl-source:22
        while j >= فجوة and ق[j - فجوة] > م:
            # apl-source:23
            ق[j] = ق[j - فجوة]
            # apl-source:24
            j = j - فجوة
        # apl-source:25
        ق[j] = م
    # apl-source:26
    فجوة = فجوة // 2
# apl-source:27
print("مفرزة:", ق)
# apl-source:28
تأكد_يساوي(ق, [1, 2, 3, 8, 9, 12, 21, 23, 34, 54], "فرز شل")
# apl-source:29
