
# apl-source:1
# مثال 3104 — متتالية أ=7×السابق+1
# apl-source:2
# Recurrence times 7 plus one
# apl-source:3
# Demonstrates: متتاليات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3104-linear-recurrence-a-n-equals-7-times-previous-plus-one.apl
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
  for ي in range(ن):
    # apl-source:21
    أ = أ * 7 + 1
  # apl-source:22
  return أ
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), 1, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(1), 8, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(2), 57, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(5), 19608, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(8), 6725601, "حالة 5")
# apl-source:29
