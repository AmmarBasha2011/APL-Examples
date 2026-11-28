
# apl-source:1
# مثال 546 — أقصى نافذة منزلقة
# apl-source:2
# Sliding window maximum
# apl-source:3
# Demonstrates: نافذة منزلقة، قائمة رتيبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/546-sliding-window-max.apl
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
# أقصى نافذة منزلقة بقائمة رتيبة
# apl-source:15
def أقصى_نوافذ(ق, ك):
    # apl-source:16
    نتائج = list()
    # apl-source:17
    فهارس = list()
    # apl-source:18
    for i in range(len(ق)):
        # apl-source:19
        while len(فهارس) > 0 and فهارس[0] <= i - ك:
            # apl-source:20
            فهارس.pop(0)
        # apl-source:21
        while len(فهارس) > 0 and ق[فهارس[len(فهارس) - 1]] <= ق[i]:
            # apl-source:22
            فهارس.pop()
        # apl-source:23
        فهارس.append(i)
        # apl-source:24
        if i >= ك - 1:
            # apl-source:25
            نتائج.append(ق[فهارس[0]])
    # apl-source:26
    return نتائج
# apl-source:27

# apl-source:28
تأكد_يساوي(أقصى_نوافذ([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7], "النوافذ")
# apl-source:29
تأكد_يساوي(أقصى_نوافذ([9, 8, 7], 1), [9, 8, 7], "نافذة واحد")
# apl-source:30
