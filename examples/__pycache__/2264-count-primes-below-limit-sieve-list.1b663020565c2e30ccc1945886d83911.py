
# apl-source:1
# مثال 2264 — عدد الأولية بالغربال
# apl-source:2
# Count primes by sieve
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2264-count-primes-below-limit-sieve-list.apl
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
  غ = [True] * (ن + 1)
  # apl-source:20
  ع = 0
  # apl-source:21
  for ي in range(2, ن + 1):
    # apl-source:22
    if غ[ي]:
      # apl-source:23
      ع = ع + 1
      # apl-source:24
      for ك in range(ي * ي, ن + 1, ي):
        # apl-source:25
        غ[ك] = False
  # apl-source:26
  return ع
# apl-source:27

# apl-source:28
تأكد_يساوي(ف(2), 1, "حالة 1")
# apl-source:29
تأكد_يساوي(ف(10), 4, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(30), 10, "حالة 3")
# apl-source:31
تأكد_يساوي(ف(100), 25, "حالة 4")
# apl-source:32
