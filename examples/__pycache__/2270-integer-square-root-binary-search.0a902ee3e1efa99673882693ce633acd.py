
# apl-source:1
# مثال 2270 — الجذر التربيعي الصحيح
# apl-source:2
# Integer square root
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2270-integer-square-root-binary-search.apl
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
  د = 0
  # apl-source:20
  ع = ن
  # apl-source:21
  while د < ع:
    # apl-source:22
    و2 = (د + ع + 1) // 2
    # apl-source:23
    if و2 * و2 <= ن:
      # apl-source:24
      د = و2
    # apl-source:25
    else:
      # apl-source:26
      ع = و2 - 1
  # apl-source:27
  return د
# apl-source:28

# apl-source:29
تأكد_يساوي(ف(0), 0, "حالة 1")
# apl-source:30
تأكد_يساوي(ف(1), 1, "حالة 2")
# apl-source:31
تأكد_يساوي(ف(15), 3, "حالة 3")
# apl-source:32
تأكد_يساوي(ف(16), 4, "حالة 4")
# apl-source:33
تأكد_يساوي(ف(17), 4, "حالة 5")
# apl-source:34
تأكد_يساوي(ف(1000000), 1000, "حالة 6")
# apl-source:35
