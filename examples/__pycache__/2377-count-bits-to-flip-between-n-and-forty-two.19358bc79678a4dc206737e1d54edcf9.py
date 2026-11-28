
# apl-source:1
# مثال 2377 — بتات التبديل إلى 42
# apl-source:2
# Bits to flip to reach 42
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2377-count-bits-to-flip-between-n-and-forty-two.apl
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
  س = ن ^ 42
  # apl-source:20
  ع = 0
  # apl-source:21
  while س > 0:
    # apl-source:22
    ع = ع + س % 2
    # apl-source:23
    س = س // 2
  # apl-source:24
  return ع
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(0), 3, "حالة 1")
# apl-source:27
تأكد_يساوي(ف(42), 0, "حالة 2")
# apl-source:28
تأكد_يساوي(ف(7), 4, "حالة 3")
# apl-source:29
تأكد_يساوي(ف(255), 5, "حالة 4")
# apl-source:30
تأكد_يساوي(ف(1), 4, "حالة 5")
# apl-source:31
