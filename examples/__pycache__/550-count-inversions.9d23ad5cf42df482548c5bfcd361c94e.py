
# apl-source:1
# مثال 550 — عدّ المعكوسات
# apl-source:2
# Counting inversions
# apl-source:3
# Demonstrates: معكوسات، فرز دمج، عد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/550-count-inversions.apl
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
# عدّ المعكوسات بفرز الدمج
# apl-source:15
def عدّ_ودمج(ق):
    # apl-source:16
    if len(ق) <= 1:
        # apl-source:17
        return [ق, 0]
    # apl-source:18
    وسط = len(ق) // 2
    # apl-source:19
    يسار = عدّ_ودمج(ق[:وسط])
    # apl-source:20
    يمين = عدّ_ودمج(ق[وسط:])
    # apl-source:21
    مدمج = list()
    # apl-source:22
    معكوسات = يسار[1] + يمين[1]
    # apl-source:23
    i = 0
    # apl-source:24
    j = 0
    # apl-source:25
    while i < len(يسار[0]) and j < len(يمين[0]):
        # apl-source:26
        if يسار[0][i] <= يمين[0][j]:
            # apl-source:27
            مدمج.append(يسار[0][i])
            # apl-source:28
            i = i + 1
        # apl-source:29
        else:
            # apl-source:30
            مدمج.append(يمين[0][j])
            # apl-source:31
            معكوسات = معكوسات + len(يسار[0]) - i
            # apl-source:32
            j = j + 1
    # apl-source:33
    مدمج = مدمج + يسار[0][i:] + يمين[0][j:]
    # apl-source:34
    return [مدمج, معكوسات]
# apl-source:35

# apl-source:36
نتيجة = عدّ_ودمج([8, 4, 2, 1])
# apl-source:37
تأكد_يساوي(نتيجة[1], 6, "معكوسات [8,4,2,1]")
# apl-source:38
تأكد_يساوي(نتيجة[0], [1, 2, 4, 8], "الفرز سليم")
# apl-source:39
تأكد_يساوي(عدّ_ودمج([1, 2, 3])[1], 0, "مفرزة بلا معكوسات")
# apl-source:40
