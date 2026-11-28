
# apl-source:1
# مثال 1760 — عدد المسارات الفريدة في شبكة
# apl-source:2
# Unique grid paths
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1760-unique-paths-grid-count.apl
# apl-source:6

# apl-source:7
# الخلية مجموع العلوية واليسرى
# apl-source:8
# الحافة واحد
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
def مسارات_فريدة(ص, س):
  # apl-source:19
  صف = []
  # apl-source:20
  for ك in range(س):
    # apl-source:21
    صف.append(1)
  # apl-source:22
  for ي in range(1, ص):
    # apl-source:23
    for ك in range(1, س):
      # apl-source:24
      صف[ك] = صف[ك] + صف[ك - 1]
  # apl-source:25
  return صف[س - 1]
# apl-source:26

# apl-source:27
تأكد_يساوي(مسارات_فريدة(3, 7), 28, "كلاسيكية")
# apl-source:28
تأكد_يساوي(مسارات_فريدة(3, 2), 3, "صغيرة")
# apl-source:29
تأكد_يساوي(مسارات_فريدة(1, 5), 1, "صف")
# apl-source:30
