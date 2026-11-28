
# apl-source:1
# مثال 2269 — طرق التمثيل بمربعين
# apl-source:2
# Ways as sum of two squares
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2269-sum-of-two-squares-representation-count.apl
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
  for أ in range(0, ن + 1):
    # apl-source:21
    for ب in range(أ, ن + 1):
      # apl-source:22
      if أ * أ + ب * ب == ن:
        # apl-source:23
        ع = ع + 1
  # apl-source:24
  return ع
# apl-source:25

# apl-source:26
تأكد_يساوي(ف(1), 1, "حالة 1")
# apl-source:27
تأكد_يساوي(ف(2), 1, "حالة 2")
# apl-source:28
تأكد_يساوي(ف(5), 1, "حالة 3")
# apl-source:29
تأكد_يساوي(ف(25), 2, "حالة 4")
# apl-source:30
تأكد_يساوي(ف(50), 2, "حالة 5")
# apl-source:31
