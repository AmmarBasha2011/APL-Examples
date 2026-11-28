
# apl-source:1
# مثال 2555 — ثلاثيات مجموعها 8
# apl-source:2
# Triples summing to 8
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2555-count-triples-sum-to-8-small.apl
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
  for أ in range(1, ن + 1):
    # apl-source:21
    for ب in range(أ, ن + 1):
      # apl-source:22
      for ج in range(ب, ن + 1):
        # apl-source:23
        if أ + ب + ج == 8:
          # apl-source:24
          ع = ع + 1
  # apl-source:25
  return ع
# apl-source:26

# apl-source:27
تأكد_يساوي(ف(5), 4, "حالة 1")
# apl-source:28
تأكد_يساوي(ف(8), 5, "حالة 2")
# apl-source:29
تأكد_يساوي(ف(11), 5, "حالة 3")
# apl-source:30
