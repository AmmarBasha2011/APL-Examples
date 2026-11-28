
# apl-source:1
# مثال 516 — البحث بالاستكمال
# apl-source:2
# Interpolation search
# apl-source:3
# Demonstrates: بحث بالاستكمال، قوائم متجانسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/516-interpolation-search.apl
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
# بحث بالاستكمال في قائمة مفرزة متجانسة
# apl-source:15
def بحث_استكمال(ق, هدف):
    # apl-source:16
    منخفض = 0
    # apl-source:17
    مرتفع = len(ق) - 1
    # apl-source:18
    while منخفض <= مرتفع and هدف >= ق[منخفض] and هدف <= ق[مرتفع]:
        # apl-source:19
        if ق[مرتفع] == ق[منخفض]:
            # apl-source:20
            if ق[منخفض] == هدف:
                # apl-source:21
                return منخفض
            # apl-source:22
            return -1
        # apl-source:23
        موضع = منخفض + (هدف - ق[منخفض]) * (مرتفع - منخفض) // (ق[مرتفع] - ق[منخفض])
        # apl-source:24
        if ق[موضع] == هدف:
            # apl-source:25
            return موضع
        # apl-source:26
        elif ق[موضع] < هدف:
            # apl-source:27
            منخفض = موضع + 1
        # apl-source:28
        else:
            # apl-source:29
            مرتفع = موضع - 1
    # apl-source:30
    return -1
# apl-source:31

# apl-source:32
ق = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# apl-source:33
تأكد_يساوي(بحث_استكمال(ق, 70), 6, "استكمال: 70")
# apl-source:34
تأكد_يساوي(بحث_استكمال(ق, 10), 0, "استكمال: الطرف")
# apl-source:35
تأكد_يساوي(بحث_استكمال(ق, 55), -1, "استكمال: غائب")
# apl-source:36
