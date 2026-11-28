
# apl-source:1
# مثال 1574 — حقيبة جزئية
# apl-source:2
# Fractional knapsack value
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1574-fractional-knapsack-value.apl
# apl-source:6

# apl-source:7
# نرتب بنسبة القيمة إلى الوزن
# apl-source:8
# نملأ الحقيبة وآخر عنصر قد يؤخذ جزء منه
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
def قيمة_الحقيبة(عناصر, سعة):
  # apl-source:19
  مرتبة = []
  # apl-source:20
  for ع in عناصر:
    # apl-source:21
    مرتبة.append([ع[0] / ع[1], ع[0], ع[1]])
  # apl-source:22
  مرتبة.sort()
  # apl-source:23
  مرتبة.reverse()
  # apl-source:24
  مجموع = 0.0
  # apl-source:25
  for م in مرتبة:
    # apl-source:26
    if سعة <= 0:
      # apl-source:27
      return مجموع
    # apl-source:28
    أخذ = min(سعة, م[2])
    # apl-source:29
    مجموع = مجموع + م[0] * أخذ
    # apl-source:30
    سعة = سعة - أخذ
  # apl-source:31
  return مجموع
# apl-source:32

# apl-source:33
تأكد_يساوي(قيمة_الحقيبة([[60, 10], [100, 20], [120, 30]], 50), 240.0, "كلاسيكي")
# apl-source:34
تأكد_يساوي(قيمة_الحقيبة([[10, 5]], 2), 4.0, "جزء")
# apl-source:35
تأكد_يساوي(قيمة_الحقيبة([[10, 5]], 0), 0.0, "بلا سعة")
# apl-source:36
