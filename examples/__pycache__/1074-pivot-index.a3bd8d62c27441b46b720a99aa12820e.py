
# apl-source:1
# مثال 1074 — فهرس المحور
# apl-source:2
# Find pivot index
# apl-source:3
# Demonstrates: مجموع كلي ومجموع يسار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1074-pivot-index.apl
# apl-source:6

# apl-source:7
# نحسب المجموع الكلي مرة
# apl-source:8
# ونمرر مجموع اليسار فيكون اليمين الكل ناقص اليسار ناقص العنصر
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
def محور(ق):
  # apl-source:19
  كلي = 0
  # apl-source:20
  for س in ق:
    # apl-source:21
    كلي = كلي + س
  # apl-source:22
  يسار = 0
  # apl-source:23
  for ع in range(len(ق)):
    # apl-source:24
    if يسار == ((كلي - يسار) - ق[ع]):
      # apl-source:25
      return ع
    # apl-source:26
    يسار = يسار + ق[ع]
  # apl-source:27
  return -1
# apl-source:28

# apl-source:29
تأكد_يساوي(محور([1, 7, 3, 6, 5, 6]), 3, "ثلاثة")
# apl-source:30
تأكد_يساوي(محور([1, 2, 3]), -1, "لا محور")
# apl-source:31
تأكد_يساوي(محور([2, 1, -1]), 0, "في البداية")
# apl-source:32
