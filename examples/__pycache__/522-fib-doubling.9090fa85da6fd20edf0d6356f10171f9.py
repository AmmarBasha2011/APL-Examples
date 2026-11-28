
# apl-source:1
# مثال 522 — فيبوناتشي بالمضاعفة السريعة
# apl-source:2
# Fibonacci by fast doubling
# apl-source:3
# Demonstrates: مضاعفة سريعة، فيبوناتشي لوغاريتمي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/522-fib-doubling.apl
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
# فيبوناتشي بالمضاعفة السريعة O(log n)
# apl-source:15
def فيب_سريع(ن):
    # apl-source:16
    if ن == 0:
        # apl-source:17
        return [0, 1]
    # apl-source:18
    نصف = فيب_سريع(ن // 2)
    # apl-source:19
    أ = نصف[0]
    # apl-source:20
    ب = نصف[1]
    # apl-source:21
    ج = أ * (2 * ب - أ)
    # apl-source:22
    د = أ * أ + ب * ب
    # apl-source:23
    if ن % 2 == 0:
        # apl-source:24
        return [ج, د]
    # apl-source:25
    return [د, ج + د]
# apl-source:26

# apl-source:27
تأكد_يساوي(فيب_سريع(10)[0], 55, "فيب 10")
# apl-source:28
تأكد_يساوي(فيب_سريع(50)[0], 12586269025, "فيب 50")
# apl-source:29
تأكد_يساوي(فيب_سريع(0)[0], 0, "فيب 0")
# apl-source:30
