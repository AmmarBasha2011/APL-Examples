
# apl-source:1
# مثال 1269 — قراءة قطرية
# apl-source:2
# Diagonal traverse
# apl-source:3
# Demonstrates: شبكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1269-diagonal-traverse.apl
# apl-source:6

# apl-source:7
# كل قطر مجموع صفه وعموده ثابت
# apl-source:8
# نعكس الأقطار الزوجية
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
def اقطار(م):
  # apl-source:19
  if len(م) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ر_ = len(م)
  # apl-source:22
  ك_ = len(م[0])
  # apl-source:23
  ناتج = []
  # apl-source:24
  for مج in range(ر_ + ك_ - 1):
    # apl-source:25
    قطر = []
    # apl-source:26
    for ص in range(ر_):
      # apl-source:27
      ج = مج - ص
      # apl-source:28
      if (ج >= 0) and (ج < ك_):
        # apl-source:29
        قطر = قطر + [م[ص][ج]]
    # apl-source:30
    if مج % 2 == 0:
      # apl-source:31
      قطر.reverse()
    # apl-source:32
    ناتج = ناتج + قطر
  # apl-source:33
  return ناتج
# apl-source:34

# apl-source:35
تأكد_يساوي(اقطار([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9], "ثلاثة في ثلاثة")
# apl-source:36
تأكد_يساوي(اقطار([[1,2],[3,4]]), [1,2,3,4], "اثنان")
# apl-source:37
تأكد_يساوي(اقطار([]), [], "فارغة")
# apl-source:38
