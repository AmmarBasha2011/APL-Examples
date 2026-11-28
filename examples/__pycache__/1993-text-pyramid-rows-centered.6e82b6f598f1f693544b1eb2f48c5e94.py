
# apl-source:1
# مثال 1993 — هرم نصي من النجوم
# apl-source:2
# Text star pyramid
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1993-text-pyramid-rows-centered.apl
# apl-source:6

# apl-source:7
# # الصف i فيه 2i-1 نجمة
# apl-source:8
# # ونملأ يساره بمسافات n-i
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
def هرم(ن):
  # apl-source:19
  صفوف = []
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    صفوف = صفوف + [" " * (ن - ك) + "*" * (2 * ك - 1)]
  # apl-source:22
  return صفوف
# apl-source:23

# apl-source:24
تأكد_يساوي(هرم(3), ["  *", " ***", "*****"], "ثلاثة صفوف")
# apl-source:25
تأكد_يساوي(هرم(1), ["*"], "صف واحد")
# apl-source:26
تأكد_يساوي(هرم(0), [], "فارغ")
# apl-source:27
