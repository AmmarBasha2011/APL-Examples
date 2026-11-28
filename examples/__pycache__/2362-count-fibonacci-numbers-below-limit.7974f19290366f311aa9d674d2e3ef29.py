
# apl-source:1
# مثال 2362 — عدد فيبوناتشي تحت حد
# apl-source:2
# Count Fibonacci below limit
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2362-count-fibonacci-numbers-below-limit.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  أ = 1
  # apl-source:20
  ب = 2
  # apl-source:21
  ع = 0
  # apl-source:22
  while أ < ن:
    # apl-source:23
    ع = ع + 1
    # apl-source:24
    أ, ب = ب, أ + ب
  # apl-source:25
  return ع
# apl-source:26

# apl-source:27
تأكد_يساوي(ف(2), 1, "حالة 1")
# apl-source:28
تأكد_يساوي(ف(10), 5, "حالة 2")
# apl-source:29
تأكد_يساوي(ف(100), 10, "حالة 3")
# apl-source:30
تأكد_يساوي(ف(1000), 15, "حالة 4")
# apl-source:31
