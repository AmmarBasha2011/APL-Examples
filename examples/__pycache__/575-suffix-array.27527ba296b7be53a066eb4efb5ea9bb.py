
# apl-source:1
# مثال 575 — مصفوفة السوابق
# apl-source:2
# Suffix array
# apl-source:3
# Demonstrates: سوابق، فرز، بحث في نص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/575-suffix-array.apl
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
# مصفوفة اللواحق: فرز كل اللواحق والبحث الثنائي فيها
# apl-source:15
def مصفوفة_لواحق(نص):
    # apl-source:16
    لواحق = list()
    # apl-source:17
    for i in range(len(نص)):
        # apl-source:18
        لواحق.append([نص[i:], i])
    # apl-source:19
    return sorted(لواحق)
# apl-source:20

# apl-source:21
def بحث(نص, نمط):
    # apl-source:22
    م = مصفوفة_لواحق(نص)
    # apl-source:23
    ب = 0
    # apl-source:24
    ن = len(م) - 1
    # apl-source:25
    while ب <= ن:
        # apl-source:26
        وسط = (ب + ن) // 2
        # apl-source:27
        مقطع = م[وسط][0][:len(نمط)]
        # apl-source:28
        if مقطع == نمط:
            # apl-source:29
            return م[وسط][1]
        # apl-source:30
        elif مقطع < نمط:
            # apl-source:31
            ب = وسط + 1
        # apl-source:32
        else:
            # apl-source:33
            ن = وسط - 1
    # apl-source:34
    return -1
# apl-source:35

# apl-source:36
نتيجة = مصفوفة_لواحق("banana")
# apl-source:37
print("اللواحق مفرزة:", نتيجة)
# apl-source:38
تأكد_يساوي(بحث("banana", "nan"), 2, "nan عند 2")
# apl-source:39
تأكد_يساوي(بحث("banana", "ana"), 1, "ana عند 1")
# apl-source:40
تأكد_يساوي(بحث("banana", "xyz"), -1, "غائب")
# apl-source:41
