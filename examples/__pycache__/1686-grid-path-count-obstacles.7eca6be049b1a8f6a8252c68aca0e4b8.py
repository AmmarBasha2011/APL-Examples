
# apl-source:1
# مثال 1686 — مسارات الشبكة مع عوائق
# apl-source:2
# Grid paths with obstacles
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1686-grid-path-count-obstacles.apl
# apl-source:6

# apl-source:7
# الخلية المحجوبة تعطي صفراً
# apl-source:8
# غير ذلك مجموع العلوية واليسرى
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
def مسارات(شبكة):
  # apl-source:19
  ص = len(شبكة)
  # apl-source:20
  س = len(شبكة[0])
  # apl-source:21
  جدول = []
  # apl-source:22
  for ي in range(ص):
    # apl-source:23
    صف = []
    # apl-source:24
    for ك in range(س):
      # apl-source:25
      صف.append(0)
    # apl-source:26
    جدول.append(صف)
  # apl-source:27
  for ي in range(ص):
    # apl-source:28
    for ك in range(س):
      # apl-source:29
      if شبكة[ي][ك] == 1:
        # apl-source:30
        جدول[ي][ك] = 0
      # apl-source:31
      elif ي == 0 and ك == 0:
        # apl-source:32
        جدول[ي][ك] = 1
      # apl-source:33
      else:
        # apl-source:34
        مجموع = 0
        # apl-source:35
        if ي > 0:
          # apl-source:36
          مجموع = مجموع + جدول[ي - 1][ك]
        # apl-source:37
        if ك > 0:
          # apl-source:38
          مجموع = مجموع + جدول[ي][ك - 1]
        # apl-source:39
        جدول[ي][ك] = مجموع
  # apl-source:40
  return جدول[ص - 1][س - 1]
# apl-source:41

# apl-source:42
تأكد_يساوي(مسارات([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2, "عائق وسط")
# apl-source:43
تأكد_يساوي(مسارات([[0, 0], [0, 0]]), 2, "بلا عوائق")
# apl-source:44
تأكد_يساوي(مسارات([[0, 1], [0, 0]]), 1, "عائق")
# apl-source:45
