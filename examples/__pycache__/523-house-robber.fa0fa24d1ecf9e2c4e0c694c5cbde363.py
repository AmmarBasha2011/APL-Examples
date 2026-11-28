
# apl-source:1
# مثال 523 — لص المنازل
# apl-source:2
# House robber DP
# apl-source:3
# Demonstrates: برمجة ديناميكية، لص المنازل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/523-house-robber.apl
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
# لص المنازل: أقصى مجموع دون جيران (برمجة ديناميكية)
# apl-source:15
def أقصى_سرقة(بيوت):
    # apl-source:16
    سابق2 = 0
    # apl-source:17
    سابق1 = 0
    # apl-source:18
    for مال in بيوت:
        # apl-source:19
        حالي = max(سابق1, سابق2 + مال)
        # apl-source:20
        سابق2 = سابق1
        # apl-source:21
        سابق1 = حالي
    # apl-source:22
    return سابق1
# apl-source:23

# apl-source:24
تأكد_يساوي(أقصى_سرقة([2, 7, 9, 3, 1]), 12, "المثال الكلاسيكي")
# apl-source:25
تأكد_يساوي(أقصى_سرقة([1, 2, 3, 1]), 4, "مثال ثان")
# apl-source:26
تأكد_يساوي(أقصى_سرقة([5]), 5, "بيت واحد")
# apl-source:27
