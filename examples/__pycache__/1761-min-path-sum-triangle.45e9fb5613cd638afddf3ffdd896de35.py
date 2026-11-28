
# apl-source:1
# مثال 1761 — أقل مجموع مسار في مثلث
# apl-source:2
# Minimum path sum in a triangle
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1761-min-path-sum-triangle.apl
# apl-source:6

# apl-source:7
# نحسب من الأسفل للأعلى
# apl-source:8
# كل خلية تضيف الأصغر من تحتها
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
def أقل_مسار(مثلث):
  # apl-source:19
  ن = len(مثلث)
  # apl-source:20
  حالي = []
  # apl-source:21
  for ع in مثلث[ن - 1]:
    # apl-source:22
    حالي.append(ع)
  # apl-source:23
  for ي in range(ن - 2, -1, -1):
    # apl-source:24
    for ك in range(ي + 1):
      # apl-source:25
      حالي[ك] = مثلث[ي][ك] + min(حالي[ك], حالي[ك + 1])
  # apl-source:26
  return حالي[0]
# apl-source:27

# apl-source:28
تأكد_يساوي(أقل_مسار([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11, "كلاسيكي")
# apl-source:29
تأكد_يساوي(أقل_مسار([[5]]), 5, "قمة")
# apl-source:30
