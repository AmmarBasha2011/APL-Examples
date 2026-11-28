
# apl-source:1
# مثال 584 — حقيبة غير محدودة
# apl-source:2
# Unbounded knapsack
# apl-source:3
# Demonstrates: حقيبة ظهر، عناصر متكررة، برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/584-unbounded-knapsack.apl
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
# حقيبة غير مقيدة: كل عنصر يتكرر
# apl-source:15
def أقصى_قيمة(أوزان, قيم, سعة):
    # apl-source:16
    أفضل = [0] * (سعة + 1)
    # apl-source:17
    for وزن in range(1, سعة + 1):
        # apl-source:18
        for i in range(len(أوزان)):
            # apl-source:19
            if أوزان[i] <= وزن:
                # apl-source:20
                if أفضل[وزن - أوزان[i]] + قيم[i] > أفضل[وزن]:
                    # apl-source:21
                    أفضل[وزن] = أفضل[وزن - أوزان[i]] + قيم[i]
    # apl-source:22
    return أفضل[سعة]
# apl-source:23

# apl-source:24
تأكد_يساوي(أقصى_قيمة([1, 3, 4, 5], [10, 40, 50, 70], 8), 110, "5+3")
# apl-source:25
تأكد_يساوي(أقصى_قيمة([5, 10], [10, 30], 3), 0, "لا شيء يدخل")
# apl-source:26
تأكد_يساوي(أقصى_قيمة([2], [5], 7), 15, "ثلاث قطع من نفس النوع")
# apl-source:27
