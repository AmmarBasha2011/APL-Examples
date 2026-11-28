
# apl-source:1
# مثال 2182 — أكبر عامل أولي
# apl-source:2
# Largest prime factor
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2182-largest-prime-factor-simple.apl
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
  د = 2
  # apl-source:20
  ك = 1
  # apl-source:21
  while ن > 1:
    # apl-source:22
    if ن % د == 0:
      # apl-source:23
      ك = د
      # apl-source:24
      ن = ن // د
    # apl-source:25
    else:
      # apl-source:26
      د = د + 1
  # apl-source:27
  return ك
# apl-source:28

# apl-source:29
تأكد_يساوي(ف(2), 2, "حالة 2")
# apl-source:30
تأكد_يساوي(ف(12), 3, "حالة 12")
# apl-source:31
تأكد_يساوي(ف(13195), 29, "حالة 13195")
# apl-source:32
تأكد_يساوي(ف(97), 97, "حالة 97")
# apl-source:33
تأكد_يساوي(ف(1000), 5, "حالة 1000")
# apl-source:34
