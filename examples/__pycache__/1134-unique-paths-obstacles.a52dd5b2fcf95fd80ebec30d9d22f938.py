
# apl-source:1
# مثال 1134 — مسارات مع عوائق
# apl-source:2
# Unique paths with obstacles
# apl-source:3
# Demonstrates: جدول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1134-unique-paths-obstacles.apl
# apl-source:6

# apl-source:7
# كل خانة تساوي مسارات الأعلى والأيسر
# apl-source:8
# والعائق صفر مسارات
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
def مسارات(ش):
  # apl-source:19
  ص = len(ش)
  # apl-source:20
  ج = len(ش[0])
  # apl-source:21
  د = []
  # apl-source:22
  for ر in range(ص):
    # apl-source:23
    د = د + [[0] * ج]
  # apl-source:24
  for ر in range(ص):
    # apl-source:25
    for ك in range(ج):
      # apl-source:26
      if ش[ر][ك] == 1:
        # apl-source:27
        د[ر][ك] = 0
      # apl-source:28
      elif (ر == 0) and (ك == 0):
        # apl-source:29
        د[ر][ك] = 1
      # apl-source:30
      else:
        # apl-source:31
        من_اعلى = 0
        # apl-source:32
        من_يسار = 0
        # apl-source:33
        if ر > 0:
          # apl-source:34
          من_اعلى = د[ر - 1][ك]
        # apl-source:35
        if ك > 0:
          # apl-source:36
          من_يسار = د[ر][ك - 1]
        # apl-source:37
        د[ر][ك] = من_اعلى + من_يسار
  # apl-source:38
  return د[ص - 1][ج - 1]
# apl-source:39

# apl-source:40
تأكد_يساوي(مسارات([[0,0,0],[0,1,0],[0,0,0]]), 2, "عائق في الوسط")
# apl-source:41
تأكد_يساوي(مسارات([[0,1],[0,0]]), 1, "عائق صغير")
# apl-source:42
تأكد_يساوي(مسارات([[1,0]]), 0, "البداية مسدودة")
# apl-source:43
تأكد_يساوي(مسارات([[0,0,0],[0,0,0],[0,0,0]]), 6, "بلا عوائق")
# apl-source:44
