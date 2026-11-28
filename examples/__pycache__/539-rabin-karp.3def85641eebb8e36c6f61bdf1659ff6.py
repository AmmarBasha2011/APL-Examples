
# apl-source:1
# مثال 539 — بحث رابين-كارب
# apl-source:2
# Rabin-Karp search
# apl-source:3
# Demonstrates: تجزئة دوارة، مطابقة أنماط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/539-rabin-karp.apl
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
# بحث رابين-كارب بالتجزئة الدوارة
# apl-source:15
def بحث_رابين(نص, نمط):
    # apl-source:16
    أساس = 256
    # apl-source:17
    معيار = 101
    # apl-source:18
    ط = len(نمط)
    # apl-source:19
    تجزئة_نمط = 0
    # apl-source:20
    تجزئة_نافذة = 0
    # apl-source:21
    عالي = 1
    # apl-source:22
    for i in range(ط - 1):
        # apl-source:23
        عالي = (عالي * أساس) % معيار
    # apl-source:24
    for i in range(ط):
        # apl-source:25
        تجزئة_نمط = (أساس * تجزئة_نمط + ord(نمط[i])) % معيار
        # apl-source:26
        تجزئة_نافذة = (أساس * تجزئة_نافذة + ord(نص[i])) % معيار
    # apl-source:27
    for i in range(len(نص) - ط + 1):
        # apl-source:28
        if تجزئة_نمط == تجزئة_نافذة:
            # apl-source:29
            if نص[i:i+ط] == نمط:
                # apl-source:30
                return i
        # apl-source:31
        if i < len(نص) - ط:
            # apl-source:32
            تجزئة_نافذة = (أساس * (تجزئة_نافذة - ord(نص[i]) * عالي) + ord(نص[i + ط])) % معيار
            # apl-source:33
            if تجزئة_نافذة < 0:
                # apl-source:34
                تجزئة_نافذة = تجزئة_نافذة + معيار
    # apl-source:35
    return -1
# apl-source:36

# apl-source:37
تأكد_يساوي(بحث_رابين("abxabcabcaby", "abcaby"), 6, "رابين-كارب: موجود")
# apl-source:38
تأكد_يساوي(بحث_رابين("aaaaab", "aab"), 3, "رابين-كارب: تكرارات")
# apl-source:39
تأكد_يساوي(بحث_رابين("hello", "zz"), -1, "رابين-كارب: غائب")
# apl-source:40
