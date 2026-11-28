
# apl-source:1
# مثال 525 — عدّ الجزر بالملء الغامر
# apl-source:2
# Flood fill island counting
# apl-source:3
# Demonstrates: ملء غامر، عدّ الجزر، شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/525-flood-fill-islands.apl
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
# عدّ الجزر بملء غامر على شبكة
# apl-source:15
شبكة = [[1, 1, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]
# apl-source:16
صفوف = 4
# apl-source:17
أعمدة = 5
# apl-source:18

# apl-source:19
def اغمر(ص, ع):
    # apl-source:20
    if ص < 0 or ص >= صفوف or ع < 0 or ع >= أعمدة:
        # apl-source:21
        return
    # apl-source:22
    if شبكة[ص][ع] != 1:
        # apl-source:23
        return
    # apl-source:24
    شبكة[ص][ع] = 2
    # apl-source:25
    اغمر(ص + 1, ع)
    # apl-source:26
    اغمر(ص - 1, ع)
    # apl-source:27
    اغمر(ص, ع + 1)
    # apl-source:28
    اغمر(ص, ع - 1)
# apl-source:29

# apl-source:30
جزر = 0
# apl-source:31
for ص in range(صفوف):
    # apl-source:32
    for ع in range(أعمدة):
        # apl-source:33
        if شبكة[ص][ع] == 1:
            # apl-source:34
            جزر = جزر + 1
            # apl-source:35
            اغمر(ص, ع)
# apl-source:36

# apl-source:37
print("عدد الجزر:", جزر)
# apl-source:38
تأكد_يساوي(جزر, 5, "خمس جزر")
# apl-source:39
