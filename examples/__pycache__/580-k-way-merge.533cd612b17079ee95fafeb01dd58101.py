
# apl-source:1
# مثال 580 — دمج ك-قائمة
# apl-source:2
# K-way merge
# apl-source:3
# Demonstrates: دمج، كومة، قوائم مرتبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/580-k-way-merge.apl
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
# دمج ك قائم مفرزة بمؤشرات
# apl-source:15
def دمج_متعدد(قوائم):
    # apl-source:16
    مؤشرات = [0] * len(قوائم)
    # apl-source:17
    نتيجة = list()
    # apl-source:18
    while True:
        # apl-source:19
        أفضل = -1
        # apl-source:20
        أقل = 999999999
        # apl-source:21
        for i in range(len(قوائم)):
            # apl-source:22
            if مؤشرات[i] < len(قوائم[i]):
                # apl-source:23
                if قوائم[i][مؤشرات[i]] < أقل:
                    # apl-source:24
                    أقل = قوائم[i][مؤشرات[i]]
                    # apl-source:25
                    أفضل = i
        # apl-source:26
        if أفضل == -1:
            # apl-source:27
            break
        # apl-source:28
        نتيجة.append(أقل)
        # apl-source:29
        مؤشرات[أفضل] = مؤشرات[أفضل] + 1
    # apl-source:30
    return نتيجة
# apl-source:31

# apl-source:32
تأكد_يساوي(دمج_متعدد([[1, 4, 7], [2, 5, 8], [3, 6, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9], "ثلاث قوائم")
# apl-source:33
تأكد_يساوي(دمج_متعدد([[], [1], []]), [1], "قوائم فارغة")
# apl-source:34
تأكد_يساوي(دمج_متعدد([[10, 20], [5, 15, 25], [1]]), [1, 5, 10, 15, 20, 25], "أطوال مختلفة")
# apl-source:35
