
# apl-source:1
# مثال 542 — ترميز هافمان
# apl-source:2
# Huffman coding
# apl-source:3
# Demonstrates: ضغط، أكواد متغيرة الطول، شجرة هافمان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/542-huffman-coding.apl
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
# ترميز هافمان: شجرة أكواد متغيرة الطول
# apl-source:15
نص = "abaabcaaaa"
# apl-source:16
تكرار = dict()
# apl-source:17
for حرف in نص:
    # apl-source:18
    if حرف in تكرار:
        # apl-source:19
        تكرار[حرف] = تكرار[حرف] + 1
    # apl-source:20
    else:
        # apl-source:21
        تكرار[حرف] = 1
# apl-source:22

# apl-source:23
أكواد = dict()
# apl-source:24
for حرف in تكرار:
    # apl-source:25
    أكواد[حرف] = ""
# apl-source:26

# apl-source:27
while len(تكرار) > 1:
    # apl-source:28
    مفاتيح = sorted(list(تكرار))
    # apl-source:29
    مفاتيح = sorted(مفاتيح)
    # apl-source:30
    أ1 = ""
    # apl-source:31
    أ2 = ""
    # apl-source:32
    ق1 = 999999
    # apl-source:33
    ق2 = 999999
    # apl-source:34
    for مفتاح in مفاتيح:
        # apl-source:35
        if تكرار[مفتاح] < ق1:
            # apl-source:36
            أ2 = أ1
            # apl-source:37
            ق2 = ق1
            # apl-source:38
            أ1 = مفتاح
            # apl-source:39
            ق1 = تكرار[مفتاح]
        # apl-source:40
        elif تكرار[مفتاح] < ق2:
            # apl-source:41
            أ2 = مفتاح
            # apl-source:42
            ق2 = تكرار[مفتاح]
    # apl-source:43
    for حرف in أ1:
        # apl-source:44
        أكواد[حرف] = "0" + أكواد[حرف]
    # apl-source:45
    for حرف in أ2:
        # apl-source:46
        أكواد[حرف] = "1" + أكواد[حرف]
    # apl-source:47
    جديد = dict()
    # apl-source:48
    جديد[أ1 + أ2] = ق1 + ق2
    # apl-source:49
    for مفتاح in تكرار:
        # apl-source:50
        if مفتاح != أ1 and مفتاح != أ2:
            # apl-source:51
            جديد[مفتاح] = تكرار[مفتاح]
    # apl-source:52
    تكرار = جديد
# apl-source:53

# apl-source:54
print("الأكواد:", أكواد)
# apl-source:55
مرمز = ""
# apl-source:56
for حرف in نص:
    # apl-source:57
    مرمز = مرمز + أكواد[حرف]
# apl-source:58
print("المرمز:", مرمز)
# apl-source:59
print("الطول:", len(مرمز), "بت بدلاً من", len(نص) * 8)
# apl-source:60
تأكد_يساوي(len(أكواد["a"]), 1, "الأكثر تكراراً أقصر كود")
# apl-source:61
تأكد_يساوي(len(مرمز), 13, "طول الترميز")
# apl-source:62
