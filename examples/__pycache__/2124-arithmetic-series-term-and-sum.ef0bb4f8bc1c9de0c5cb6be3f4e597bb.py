
# apl-source:1
# مثال 2124 — الحد العام ومجموع متتالية حسابية
# apl-source:2
# Arithmetic series term and sum
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2124-arithmetic-series-term-and-sum.apl
# apl-source:6

# apl-source:7
# # المجموع نصف عدد الحدود في مجموع الطرفين
# apl-source:8
# # نرجع الحد والمجموع
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def حسابية(ا, د, ن):
  # apl-source:19
  حد = ا + (ن - 1) * د
  # apl-source:20
  return [حد, ن * (ا + حد) // 2]
# apl-source:21

# apl-source:22
تأكد_يساوي(حسابية(3, 4, 5), [19, 55], "٣،٤")
# apl-source:23
تأكد_يساوي(حسابية(1, 1, 100), [100, 5050], "١ إلى ١٠٠")
# apl-source:24
تأكد_يساوي(حسابية(10, 0, 3), [10, 30], "ثابتة")
# apl-source:25
