
# apl-source:1
# مثال 1753 — كل أزواج القائمة
# apl-source:2
# All pairs from a list
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1753-combinations-of-size-two.apl
# apl-source:6

# apl-source:7
# حلقتان متداخلتان
# apl-source:8
# الثانية تبدأ بعد الأولى
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
def أزواج(ق):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ي in range(len(ق)):
    # apl-source:21
    for ك in range(ي + 1, len(ق)):
      # apl-source:22
      ناتج.append([ق[ي], ق[ك]])
  # apl-source:23
  return ناتج
# apl-source:24

# apl-source:25
تأكد_يساوي(أزواج([1, 2, 3]), [[1, 2], [1, 3], [2, 3]], "ثلاثة")
# apl-source:26
تأكد_يساوي(أزواج([1]), [], "عنصر")
# apl-source:27
تأكد_يساوي(len(أزواج([1, 2, 3, 4, 5])), 10, "خمسة")
# apl-source:28
