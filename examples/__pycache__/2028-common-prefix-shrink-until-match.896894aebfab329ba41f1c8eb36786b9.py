
# apl-source:1
# مثال 2028 — أطول بادئة مشتركة بالتقليص
# apl-source:2
# Common prefix by shrinking
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2028-common-prefix-shrink-until-match.apl
# apl-source:6

# apl-source:7
# # نبدأ بالكلمة الأولى
# apl-source:8
# # ونقصها حرفا حرفا عند عدم التطابق
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
def بادئة(كلمات):
  # apl-source:19
  if len(كلمات) == 0:
    # apl-source:20
    return ""
  # apl-source:21
  ب = كلمات[0]
  # apl-source:22
  for ك in كلمات:
    # apl-source:23
    while ك.startswith(ب) == False:
      # apl-source:24
      ب = ب[:-1]
  # apl-source:25
  return ب
# apl-source:26

# apl-source:27
تأكد_يساوي(بادئة(["flower", "flow", "flight"]), "fl", "fl")
# apl-source:28
تأكد_يساوي(بادئة(["dog", "car"]), "", "لا توجد")
# apl-source:29
تأكد_يساوي(بادئة(["a"]), "a", "كلمة")
# apl-source:30
تأكد_يساوي(بادئة([]), "", "فارغة")
# apl-source:31
