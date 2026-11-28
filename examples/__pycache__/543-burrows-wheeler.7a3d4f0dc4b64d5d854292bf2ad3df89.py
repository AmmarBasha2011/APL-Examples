
# apl-source:1
# مثال 543 — تحويل بوروز-ويلر
# apl-source:2
# Burrows-Wheeler transform
# apl-source:3
# Demonstrates: BWT، تحويل وعكس، فرز دورانات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/543-burrows-wheeler.apl
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
# تحويل بوروز-ويلر وعكسه
# apl-source:15
def حوّل(نص):
    # apl-source:16
    ممدد = نص + "$"
    # apl-source:17
    دورانات = list()
    # apl-source:18
    for i in range(len(ممدد)):
        # apl-source:19
        دورانات.append(ممدد[i:] + ممدد[:i])
    # apl-source:20
    دورانات = sorted(دورانات)
    # apl-source:21
    أخير = ""
    # apl-source:22
    for د in دورانات:
        # apl-source:23
        أخير = أخير + د[len(د) - 1]
    # apl-source:24
    return أخير
# apl-source:25

# apl-source:26
def اعكس(أخير):
    # apl-source:27
    ن = len(أخير)
    # apl-source:28
    جدول = [""] * ن
    # apl-source:29
    for جولة in range(ن):
        # apl-source:30
        for i in range(ن):
            # apl-source:31
            جدول[i] = أخير[i] + جدول[i]
        # apl-source:32
        جدول = sorted(جدول)
    # apl-source:33
    for صف in جدول:
        # apl-source:34
        if صف[ن - 1] == "$":
            # apl-source:35
            return صف[:ن - 1]
    # apl-source:36
    return ""
# apl-source:37

# apl-source:38
نتيجة = حوّل("BANANA")
# apl-source:39
print("التحويل:", نتيجة)
# apl-source:40
تأكد_يساوي(نتيجة, "ANNB$AA", "BWT نص BANANA")
# apl-source:41
تأكد_يساوي(اعكس(نتيجة), "BANANA", "العكس يرجع الأصل")
# apl-source:42
