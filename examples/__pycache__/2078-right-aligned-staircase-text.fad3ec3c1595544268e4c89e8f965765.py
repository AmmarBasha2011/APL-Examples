
# apl-source:1
# مثال 2078 — درج نصي محاذى لليمين
# apl-source:2
# Right aligned staircase
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2078-right-aligned-staircase-text.apl
# apl-source:6

# apl-source:7
# # المسافات في اليسار والعلامات في اليمين
# apl-source:8
# # الصف الأخير كله علامات
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
def درج(ن):
  # apl-source:19
  خرج = []
  # apl-source:20
  for ك in range(1, ن + 1):
    # apl-source:21
    خرج = خرج + [" " * (ن - ك) + "#" * ك]
  # apl-source:22
  return خرج
# apl-source:23

# apl-source:24
تأكد_يساوي(درج(3), ["  #", " ##", "###"], "٣")
# apl-source:25
تأكد_يساوي(درج(1), ["#"], "١")
# apl-source:26
