
# apl-source:1
# مثال 535 — فاتورة بضريبة القيمة المضافة
# apl-source:2
# VAT invoice
# apl-source:3
# Demonstrates: ضريبة قيمة مضافة، فاتورة بنود
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/535-vat-invoice.apl
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
# فاتورة بضريبة قيمة مضافة 14%
# apl-source:15
بنود = [["طابعة", 1200, 1], ["حبر", 350, 2], ["ورق", 90, 5]]
# apl-source:16
إجمالي_قبل = 0
# apl-source:17
for بند in بنود:
    # apl-source:18
    إجمالي_قبل = إجمالي_قبل + بند[1] * بند[2]
    # apl-source:19
    print(بند[0], "×", بند[2], "=", بند[1] * بند[2])
# apl-source:20
ضريبة = إجمالي_قبل * 14 / 100
# apl-source:21
إجمالي = إجمالي_قبل + ضريبة
# apl-source:22
print("قبل الضريبة:", إجمالي_قبل)
# apl-source:23
print("الضريبة:", ضريبة)
# apl-source:24
print("الإجمالي:", إجمالي)
# apl-source:25
تأكد_يساوي(إجمالي_قبل, 2350, "الإجمالي قبل الضريبة")
# apl-source:26
تأكد_يساوي(ضريبة, 329, "ضريبة 14%")
# apl-source:27
تأكد_يساوي(إجمالي, 2679, "الإجمالي النهائي")
# apl-source:28
