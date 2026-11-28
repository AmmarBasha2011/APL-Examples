
# apl-source:1
# مثال 515 — فرز الحاويات
# apl-source:2
# Bucket sort
# apl-source:3
# Demonstrates: فرز الحاويات، توزيع على سلال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/515-bucket-sort.apl
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
# فرز الحاويات لأعداد بين 0 و1
# apl-source:15
ق = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51, 0.05]
# apl-source:16
حاويات = [[], [], [], [], [], [], [], [], [], []]
# apl-source:17
for س in ق:
    # apl-source:18
    حاويات[int(س * 10)].append(س)
# apl-source:19
ناتج = list()
# apl-source:20
for حاوية in حاويات:
    # apl-source:21
    for س in sorted(حاوية):
        # apl-source:22
        ناتج.append(س)
# apl-source:23
print("مفرزة:", ناتج)
# apl-source:24
تأكد_يساوي(ناتج[0], 0.05, "أصغر عنصر")
# apl-source:25
تأكد_يساوي(ناتج[7], 0.52, "أكبر عنصر")
# apl-source:26
تأكد_يساوي(len(ناتج), 8, "العدد ثابت")
# apl-source:27
