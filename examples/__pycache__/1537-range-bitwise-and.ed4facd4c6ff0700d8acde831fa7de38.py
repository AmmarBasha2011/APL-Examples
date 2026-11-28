
# apl-source:1
# مثال 1537 — AND لمجال أعداد
# apl-source:2
# Bitwise AND of a number range
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1537-range-bitwise-and.apl
# apl-source:6

# apl-source:7
# النتيجة هي البادئة المشتركة للعددين
# apl-source:8
# نزيح حتى يتساويا ثم نرجع الإزاحة
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
def و_المجال(م, ن):
  # apl-source:19
  إزاحة = 0
  # apl-source:20
  while م != ن:
    # apl-source:21
    م = م >> 1
    # apl-source:22
    ن = ن >> 1
    # apl-source:23
    إزاحة = إزاحة + 1
  # apl-source:24
  return م << إزاحة
# apl-source:25

# apl-source:26
تأكد_يساوي(و_المجال(5, 7), 4, "من خمسة لسبعة")
# apl-source:27
تأكد_يساوي(و_المجال(0, 0), 0, "صفر")
# apl-source:28
تأكد_يساوي(و_المجال(12, 15), 12, "اثنا عشر")
# apl-source:29
