
# apl-source:1
# مثال 579 — تشابه جارو-وينكلر
# apl-source:2
# Jaro-Winkler similarity
# apl-source:3
# Demonstrates: تشابه نصوص، أسماء، بادئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/579-jaro-winkler.apl
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
# تشابه جارو-وينكلر بين سلسلتين
# apl-source:15
def جارو(أ, ب):
    # apl-source:16
    نطاق_بحث = max(len(أ), len(ب)) // 2 - 1
    # apl-source:17
    if نطاق_بحث < 0:
        # apl-source:18
        نطاق_بحث = 0
    # apl-source:19
    تطابق_أ = [False] * len(أ)
    # apl-source:20
    تطابق_ب = [False] * len(ب)
    # apl-source:21
    تطابقات = 0
    # apl-source:22
    for i in range(len(أ)):
        # apl-source:23
        من = max(0, i - نطاق_بحث)
        # apl-source:24
        الى = min(len(ب), i + نطاق_بحث + 1)
        # apl-source:25
        for j in range(من, الى):
            # apl-source:26
            if not تطابق_ب[j] and أ[i] == ب[j]:
                # apl-source:27
                تطابق_أ[i] = True
                # apl-source:28
                تطابق_ب[j] = True
                # apl-source:29
                تطابقات = تطابقات + 1
                # apl-source:30
                break
    # apl-source:31
    if تطابقات == 0:
        # apl-source:32
        return 0
    # apl-source:33
    نقلات = 0
    # apl-source:34
    ك = 0
    # apl-source:35
    for i in range(len(أ)):
        # apl-source:36
        if تطابق_أ[i]:
            # apl-source:37
            while not تطابق_ب[ك]:
                # apl-source:38
                ك = ك + 1
            # apl-source:39
            if أ[i] != ب[ك]:
                # apl-source:40
                نقلات = نقلات + 1
            # apl-source:41
            ك = ك + 1
    # apl-source:42
    نقلات = نقلات // 2
    # apl-source:43
    return (تطابقات / len(أ) + تطابقات / len(ب) + (تطابقات - نقلات) / تطابقات) / 3
# apl-source:44

# apl-source:45
def وينكلر(أ, ب):
    # apl-source:46
    ج = جارو(أ, ب)
    # apl-source:47
    بادئة = 0
    # apl-source:48
    for i in range(min(4, min(len(أ), len(ب)))):
        # apl-source:49
        if أ[i] == ب[i]:
            # apl-source:50
            بادئة = بادئة + 1
    # apl-source:51
    return ج + بادئة * 0.1 * (1 - ج)
# apl-source:52

# apl-source:53
تأكد_يساوي(round(جارو("MARTHA", "MARHTA"), 3), 0.944, "جارو MARTHA/MARHTA")
# apl-source:54
تأكد_يساوي(round(وينكلر("MARTHA", "MARHTA"), 3), 0.961, "وينكلر MARTHA/MARHTA")
# apl-source:55
تأكد_يساوي(جارو("abc", "xyz"), 0, "لا تطابق")
# apl-source:56
