
# apl-source:1
# مثال 2274 — طرق صعود الدرج
# apl-source:2
# Climb stairs ways
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2274-number-of-ways-climb-stairs-steps-one-two.apl
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
  ب = 1
  # apl-source:21
  for ي in range(ن):
    # apl-source:22
    أ, ب = ب, أ + ب
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:26
تأكد_يساوي(ف(2), 2, "حالة 2")
# apl-source:27
تأكد_يساوي(ف(5), 8, "حالة 3")
# apl-source:28
تأكد_يساوي(ف(10), 89, "حالة 4")
# apl-source:29
تأكد_يساوي(ف(20), 10946, "حالة 5")
# apl-source:30
