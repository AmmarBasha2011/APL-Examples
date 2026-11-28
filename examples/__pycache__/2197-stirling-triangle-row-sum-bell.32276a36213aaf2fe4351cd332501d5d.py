
# apl-source:1
# مثال 2197 — عدد بيل
# apl-source:2
# Bell number via triangle
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2197-stirling-triangle-row-sum-bell.apl
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
  صف = [1]
  # apl-source:20
  for ي in range(ن):
    # apl-source:21
    جد = [صف[-1]]
    # apl-source:22
    for ق in صف:
      # apl-source:23
      جد = جد + [جد[-1] + ق]
    # apl-source:24
    صف = جد
  # apl-source:25
  return صف[0]
# apl-source:26

# apl-source:27
تأكد_يساوي(ف(0), 1, "حالة 0")
# apl-source:28
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(2), 2, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(3), 5, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(4), 15, "حالة 4")
# apl-source:32
تأكد_يساوي(ف(5), 52, "حالة 5")
# apl-source:33
تأكد_يساوي(ف(6), 203, "حالة 6")
# apl-source:34
تأكد_يساوي(ف(7), 877, "حالة 7")
# apl-source:35
