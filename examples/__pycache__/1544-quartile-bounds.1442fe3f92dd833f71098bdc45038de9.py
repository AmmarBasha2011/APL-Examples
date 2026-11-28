
# apl-source:1
# مثال 1544 — الربيعات
# apl-source:2
# Quartiles of a list
# apl-source:3
# Demonstrates: إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1544-quartile-bounds.apl
# apl-source:6

# apl-source:7
# نرتب القائمة
# apl-source:8
# نقسمها نصفين ونأخذ وسيط كل نصف
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
def وسيط(ق):
  # apl-source:19
  ن = len(ق)
  # apl-source:20
  if ن % 2 == 1:
    # apl-source:21
    return ق[ن // 2]
  # apl-source:22
  return (ق[ن // 2 - 1] + ق[ن // 2]) / 2
# apl-source:23

# apl-source:24
def ربيعات(أ):
  # apl-source:25
  ق = []
  # apl-source:26
  for ع in أ:
    # apl-source:27
    ق.append(ع)
  # apl-source:28
  ق.sort()
  # apl-source:29
  ن = len(ق)
  # apl-source:30
  أول = ق[0:ن // 2]
  # apl-source:31
  ثان = ق[(ن + 1) // 2:ن]
  # apl-source:32
  return [وسيط(أول), وسيط(ثان)]
# apl-source:33

# apl-source:34
تأكد_يساوي(ربيعات([1, 2, 3, 4, 5, 6, 7, 8]), [2.5, 6.5], "ثمانية")
# apl-source:35
تأكد_يساوي(ربيعات([7, 1, 3, 5, 9, 11, 13]), [3, 11], "سبعة")
# apl-source:36
