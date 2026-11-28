
# apl-source:1
# مثال 1729 — عدد العناصر الفريدة المرتبة
# apl-source:2
# Unique count in sorted array
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1729-remove-duplicates-sorted-count.apl
# apl-source:6

# apl-source:7
# القائمة مرتبة فالمكرر متجاور
# apl-source:8
# نعد التغيرات
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
def فريدة(ق):
  # apl-source:19
  if len(ق) == 0:
    # apl-source:20
    return 0
  # apl-source:21
  عد = 1
  # apl-source:22
  for ك in range(1, len(ق)):
    # apl-source:23
    if ق[ك] != ق[ك - 1]:
      # apl-source:24
      عد = عد + 1
  # apl-source:25
  return عد
# apl-source:26

# apl-source:27
تأكد_يساوي(فريدة([1, 1, 2, 3, 3, 3]), 3, "ثلاثة")
# apl-source:28
تأكد_يساوي(فريدة([]), 0, "فارغة")
# apl-source:29
تأكد_يساوي(فريدة([5, 5, 5]), 1, "كلها واحدة")
# apl-source:30
