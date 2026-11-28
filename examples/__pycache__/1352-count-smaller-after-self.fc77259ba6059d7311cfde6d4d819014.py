
# apl-source:1
# مثال 1352 — الأصغر بعد العنصر
# apl-source:2
# Count smaller numbers after self
# apl-source:3
# Demonstrates: شجرة فينويك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1352-count-smaller-after-self.apl
# apl-source:6

# apl-source:7
# نمر من اليمين إلى اليسار
# apl-source:8
# ونستخدم شجرة فينويك على رتب القيم
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
def اصغر_بعدي(أرقام):
  # apl-source:19
  قيم = sorted(أرقام)
  # apl-source:20
  رتبة = {}
  # apl-source:21
  ر = 1
  # apl-source:22
  for ق in قيم:
    # apl-source:23
    if ق not in رتبة:
      # apl-source:24
      رتبة[ق] = ر
      # apl-source:25
      ر = ر + 1
  # apl-source:26
  ن = ر
  # apl-source:27
  شجرة = [0] * (ن + 1)
  # apl-source:28
  ناتج = [0] * len(أرقام)
  # apl-source:29
  for ع in range(len(أرقام) - 1, -1, -1):
    # apl-source:30
    ك = رتبة[أرقام[ع]] - 1
    # apl-source:31
    مجموع = 0
    # apl-source:32
    while ك > 0:
      # apl-source:33
      مجموع = مجموع + شجرة[ك]
      # apl-source:34
      ك = ك - (ك & (-ك))
    # apl-source:35
    ناتج[ع] = مجموع
    # apl-source:36
    ك = رتبة[أرقام[ع]]
    # apl-source:37
    while ك <= ن:
      # apl-source:38
      شجرة[ك] = شجرة[ك] + 1
      # apl-source:39
      ك = ك + (ك & (-ك))
  # apl-source:40
  return ناتج
# apl-source:41

# apl-source:42
تأكد_يساوي(اصغر_بعدي([5,2,6,1]), [2,1,1,0], "مثال أول")
# apl-source:43
تأكد_يساوي(اصغر_بعدي([-1]), [0], "عنصر")
# apl-source:44
تأكد_يساوي(اصغر_بعدي([-1,-1]), [0,0], "متساويان")
# apl-source:45
