
# apl-source:1
# مثال 2146 — عدد السلاسل الثنائية بلا واحدين متجاورين
# apl-source:2
# Binary strings no adjacent ones
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2146-binary-strings-without-adjacent-ones-count.apl
# apl-source:6

# apl-source:7
# # نتتبع النهايات بصفر وبواحد
# apl-source:8
# # المجموع للطول ن
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
def عد(ن):
  # apl-source:19
  ا = 1
  # apl-source:20
  ب = 1
  # apl-source:21
  for ك in range(ن - 1):
    # apl-source:22
    ت = ا + ب
    # apl-source:23
    ب = ا
    # apl-source:24
    ا = ت
  # apl-source:25
  return ا + ب
# apl-source:26

# apl-source:27
تأكد_يساوي(عد(1), 2, "١")
# apl-source:28
تأكد_يساوي(عد(2), 3, "٢")
# apl-source:29
تأكد_يساوي(عد(3), 5, "٣")
# apl-source:30
تأكد_يساوي(عد(5), 13, "٥")
# apl-source:31
تأكد_يساوي(عد(10), 144, "١٠")
# apl-source:32
