
# apl-source:1
# مثال 2193 — حد تريبوناتشي
# apl-source:2
# Tribonacci nth term
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2193-tribonacci-nth-term-loop.apl
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
  أ = 0
  # apl-source:20
  ب = 0
  # apl-source:21
  ج = 1
  # apl-source:22
  for ي in range(ن):
    # apl-source:23
    أ, ب, ج = ب, ج, أ + ب + ج
  # apl-source:24
  return أ
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(0), 0, "حالة 0")
# apl-source:27
تأكد_يساوي(ف(1), 0, "حالة 1")
# apl-source:28
تأكد_يساوي(ف(2), 1, "حالة 2")
# apl-source:29
تأكد_يساوي(ف(5), 4, "حالة 5")
# apl-source:30
تأكد_يساوي(ف(10), 81, "حالة 10")
# apl-source:31
