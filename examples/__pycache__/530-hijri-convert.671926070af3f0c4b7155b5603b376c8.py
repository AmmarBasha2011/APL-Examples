
# apl-source:1
# مثال 530 — التحويل إلى التقويم الهجري
# apl-source:2
# Gregorian to Hijri conversion
# apl-source:3
# Demonstrates: تقويم هجري، الخوارزمية الكويتية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/530-hijri-convert.apl
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
# تحويل ميلادي إلى هجري (الخوارزمية الكويتية التقريبية)
# apl-source:15
def إلى_هجري(سنة, شهر, يوم):
    # apl-source:16
    أ = int((شهر - 14) / 12)
    # apl-source:17
    جد = int(1461 * (سنة + 4800 + أ) / 4) + int(367 * (شهر - 2 - 12 * أ) / 12) - int(3 * int((سنة + 4900 + أ) / 100) / 4) + يوم - 32075
    # apl-source:18
    ل = جد - 1948440 + 10632
    # apl-source:19
    ن = int((ل - 1) / 10631)
    # apl-source:20
    ل = ل - 10631 * ن + 354
    # apl-source:21
    ج = int((10985 - ل) / 5316) * int(50 * ل / 17719) + int(ل / 5670) * int(43 * ل / 15238)
    # apl-source:22
    ل = ل - int((30 - ج) / 15) * int(17719 * ج / 50) - int(ج / 16) * int(15238 * ج / 43) + 29
    # apl-source:23
    شهر_ه = int(24 * ل / 709)
    # apl-source:24
    يوم_ه = ل - int(709 * شهر_ه / 24)
    # apl-source:25
    سنة_ه = 30 * ن + ج - 30
    # apl-source:26
    return [سنة_ه, شهر_ه, يوم_ه]
# apl-source:27

# apl-source:28
نتيجة = إلى_هجري(2024, 3, 11)
# apl-source:29
print("11 مارس 2024 هجرياً:", نتيجة)
# apl-source:30
تأكد_يساوي(نتيجة, [1445, 9, 1], "أول رمضان 1445")
# apl-source:31
