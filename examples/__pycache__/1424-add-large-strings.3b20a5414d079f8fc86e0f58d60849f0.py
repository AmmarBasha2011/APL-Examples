
# apl-source:1
# مثال 1424 — جمع نصين رقميين
# apl-source:2
# Add two numeric strings
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1424-add-large-strings.apl
# apl-source:6

# apl-source:7
# نجمع من الأرقام الأخيرة مع الحمل
# apl-source:8
# ننتهي عند نفاد الرقمين والحمل
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
def اجمع_نصين(أ, ب):
  # apl-source:19
  ع = len(أ) - 1
  # apl-source:20
  ج = len(ب) - 1
  # apl-source:21
  حمل = 0
  # apl-source:22
  ناتج = ""
  # apl-source:23
  while (ع >= 0) or (ج >= 0) or (حمل > 0):
    # apl-source:24
    مجموع = حمل
    # apl-source:25
    if ع >= 0:
      # apl-source:26
      مجموع = مجموع + int(أ[ع])
      # apl-source:27
      ع = ع - 1
    # apl-source:28
    if ج >= 0:
      # apl-source:29
      مجموع = مجموع + int(ب[ج])
      # apl-source:30
      ج = ج - 1
    # apl-source:31
    ناتج = str(مجموع % 10) + ناتج
    # apl-source:32
    حمل = مجموع // 10
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(اجمع_نصين("11", "123"), "134", "ثلاثة أرقام")
# apl-source:36
تأكد_يساوي(اجمع_نصين("456", "77"), "533", "حمل")
# apl-source:37
تأكد_يساوي(اجمع_نصين("999", "1"), "1000", "حمل أخير")
# apl-source:38
