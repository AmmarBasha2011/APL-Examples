
# apl-source:1
# مثال 1880 — مجموع مستطيل بالتراكمي ثنائي البعد
# apl-source:2
# 2D prefix sum rectangle query
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1880-rectangle-sum-prefix-2d.apl
# apl-source:6

# apl-source:7
# الخلية مجموع المستطيل من البداية
# apl-source:8
# نطرح المناطق الزائدة
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
def ابن_جدول(م):
  # apl-source:19
  ص = len(م)
  # apl-source:20
  س = len(م[0])
  # apl-source:21
  ت = []
  # apl-source:22
  for ي in range(ص + 1):
    # apl-source:23
    صف = []
    # apl-source:24
    for ك in range(س + 1):
      # apl-source:25
      صف.append(0)
    # apl-source:26
    ت.append(صف)
  # apl-source:27
  for ي in range(ص):
    # apl-source:28
    for ك in range(س):
      # apl-source:29
      ت[ي + 1][ك + 1] = م[ي][ك] + ت[ي][ك + 1] + ت[ي + 1][ك] - ت[ي][ك]
  # apl-source:30
  return ت
# apl-source:31

# apl-source:32
def مجموع(ت, ص1, س1, ص2, س2):
  # apl-source:33
  return ت[ص2 + 1][س2 + 1] - ت[ص1][س2 + 1] - ت[ص2 + 1][س1] + ت[ص1][س1]
# apl-source:34

# apl-source:35
م = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# apl-source:36
ت = ابن_جدول(م)
# apl-source:37
تأكد_يساوي(مجموع(ت, 0, 0, 2, 2), 45, "كامل")
# apl-source:38
تأكد_يساوي(مجموع(ت, 1, 1, 2, 2), 28, "ركن")
# apl-source:39
تأكد_يساوي(مجموع(ت, 1, 0, 1, 2), 15, "صف")
# apl-source:40
