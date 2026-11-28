
# apl-source:1
# مثال 544 — سلم الكلمات
# apl-source:2
# Word ladder BFS
# apl-source:3
# Demonstrates: BFS، تحويل كلمات، أقصر مسار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/544-word-ladder.apl
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
# سلم الكلمات: أقصر تحويل بحرف واحد (BFS)
# apl-source:15
def سلم(بداية, نهاية, قاموس_كلمات):
    # apl-source:16
    طابور = [[بداية, 1]]
    # apl-source:17
    مزارة = [بداية]
    # apl-source:18
    while len(طابور) > 0:
        # apl-source:19
        عنصر = طابور.pop(0)
        # apl-source:20
        كلمة = عنصر[0]
        # apl-source:21
        عمق = عنصر[1]
        # apl-source:22
        if كلمة == نهاية:
            # apl-source:23
            return عمق
        # apl-source:24
        for مرشحة in قاموس_كلمات:
            # apl-source:25
            if مرشحة not in مزارة:
                # apl-source:26
                اختلاف = 0
                # apl-source:27
                for i in range(len(كلمة)):
                    # apl-source:28
                    if كلمة[i] != مرشحة[i]:
                        # apl-source:29
                        اختلاف = اختلاف + 1
                # apl-source:30
                if اختلاف == 1:
                    # apl-source:31
                    مزارة.append(مرشحة)
                    # apl-source:32
                    طابور.append([مرشحة, عمق + 1])
    # apl-source:33
    return 0
# apl-source:34

# apl-source:35
قاموس_كلمات = ["hot", "dot", "dog", "lot", "log", "cog"]
# apl-source:36
تأكد_يساوي(سلم("hit", "cog", قاموس_كلمات), 5, "hit إلى cog في 5")
# apl-source:37
تأكد_يساوي(سلم("hit", "zzz", ["hot"]), 0, "لا مسار")
# apl-source:38
