
# apl-source:1
# مثال 513 — بحث كنوث-موريس-برات
# apl-source:2
# KMP pattern search
# apl-source:3
# Demonstrates: مطابقة أنماط، جدول الفشل، بحث خطي الزمن
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/513-kmp-search.apl
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
# بحث كنوث-موريس-برات عن نمط في نص
# apl-source:15
def جدول_فشل(نمط):
    # apl-source:16
    ج = [0]
    # apl-source:17
    ط = 0
    # apl-source:18
    for i in range(1, len(نمط)):
        # apl-source:19
        while ط > 0 and نمط[i] != نمط[ط]:
            # apl-source:20
            ط = ج[ط - 1]
        # apl-source:21
        if نمط[i] == نمط[ط]:
            # apl-source:22
            ط = ط + 1
        # apl-source:23
        ج.append(ط)
    # apl-source:24
    return ج
# apl-source:25

# apl-source:26
def بحث_kmp(نص, نمط):
    # apl-source:27
    ج = جدول_فشل(نمط)
    # apl-source:28
    ط = 0
    # apl-source:29
    for i in range(len(نص)):
        # apl-source:30
        while ط > 0 and نص[i] != نمط[ط]:
            # apl-source:31
            ط = ج[ط - 1]
        # apl-source:32
        if نص[i] == نمط[ط]:
            # apl-source:33
            ط = ط + 1
        # apl-source:34
        if ط == len(نمط):
            # apl-source:35
            return i - len(نمط) + 1
    # apl-source:36
    return -1
# apl-source:37

# apl-source:38
نص = "abxabcabcaby"
# apl-source:39
print("جدول الفشل:", جدول_فشل("abcaby"))
# apl-source:40
تأكد_يساوي(بحث_kmp(نص, "abcaby"), 6, "KMP: موضع أول تطابق")
# apl-source:41
تأكد_يساوي(بحث_kmp(نص, "xyz"), -1, "KMP: نمط غائب")
# apl-source:42
