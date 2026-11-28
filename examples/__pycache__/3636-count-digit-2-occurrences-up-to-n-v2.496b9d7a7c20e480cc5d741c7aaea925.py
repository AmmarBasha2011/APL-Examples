
# apl-source:1
# مثال 3636 — عدد ظهور الرقم 2 حتى ن
# apl-source:2
# Occurrences of digit 2 up to n
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/3636-count-digit-2-occurrences-up-to-n-v2.apl
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
  ع = 0
  # apl-source:20
  for ي in range(1, ن + 1):
    # apl-source:21
    ع = ع + str(ي).count("2")
  # apl-source:22
  return ع
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(9), 1, "حالة 1")
# apl-source:25
تأكد_يساوي(ف(10), 1, "حالة 2")
# apl-source:26
تأكد_يساوي(ف(50), 15, "حالة 3")
# apl-source:27
تأكد_يساوي(ف(100), 20, "حالة 4")
# apl-source:28
تأكد_يساوي(ف(200), 41, "حالة 5")
# apl-source:29
