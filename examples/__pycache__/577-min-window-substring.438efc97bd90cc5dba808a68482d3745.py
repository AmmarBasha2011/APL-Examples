
# apl-source:1
# مثال 577 — أصغر نافذة شاملة
# apl-source:2
# Minimum window substring
# apl-source:3
# Demonstrates: نافذة منزلقة، تغطية أحرف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/577-min-window-substring.apl
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
# أصغر نافذة تحوي كل حروف النمط
# apl-source:15
def أصغر_نافذة(نص, نمط):
    # apl-source:16
    مطلوب = dict()
    # apl-source:17
    for حرف in نمط:
        # apl-source:18
        if حرف in مطلوب:
            # apl-source:19
            مطلوب[حرف] = مطلوب[حرف] + 1
        # apl-source:20
        else:
            # apl-source:21
            مطلوب[حرف] = 1
    # apl-source:22
    ناقص = len(مطلوب)
    # apl-source:23
    بداية = 0
    # apl-source:24
    أفضل = ""
    # apl-source:25
    أقل = len(نص) + 1
    # apl-source:26
    عدّاد = dict()
    # apl-source:27
    for نهاية in range(len(نص)):
        # apl-source:28
        حرف = نص[نهاية]
        # apl-source:29
        if حرف in مطلوب:
            # apl-source:30
            if حرف in عدّاد:
                # apl-source:31
                عدّاد[حرف] = عدّاد[حرف] + 1
            # apl-source:32
            else:
                # apl-source:33
                عدّاد[حرف] = 1
            # apl-source:34
            if عدّاد[حرف] == مطلوب[حرف]:
                # apl-source:35
                ناقص = ناقص - 1
        # apl-source:36
        while ناقص == 0:
            # apl-source:37
            if نهاية - بداية + 1 < أقل:
                # apl-source:38
                أقل = نهاية - بداية + 1
                # apl-source:39
                أفضل = نص[بداية:نهاية + 1]
            # apl-source:40
            أول = نص[بداية]
            # apl-source:41
            if أول in مطلوب:
                # apl-source:42
                if عدّاد[أول] == مطلوب[أول]:
                    # apl-source:43
                    ناقص = ناقص + 1
                # apl-source:44
                عدّاد[أول] = عدّاد[أول] - 1
            # apl-source:45
            بداية = بداية + 1
    # apl-source:46
    return أفضل
# apl-source:47

# apl-source:48
تأكد_يساوي(أصغر_نافذة("ADOBECODEBANC", "ABC"), "BANC", "الكلاسيكي")
# apl-source:49
تأكد_يساوي(أصغر_نافذة("aa", "aa"), "aa", "تكرار")
# apl-source:50
تأكد_يساوي(أصغر_نافذة("abc", "d"), "", "مستحيل")
# apl-source:51
