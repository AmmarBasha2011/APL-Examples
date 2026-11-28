
# apl-source:1
# مثال 1173 — وسيط النافذة
# apl-source:2
# Sliding window median
# apl-source:3
# Demonstrates: نافذة مرتبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1173-sliding-window-median.apl
# apl-source:6

# apl-source:7
# نحتفظ بالنافذة مرتبة
# apl-source:8
# ونحسب الوسيط من منتصفها
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
    return ق[ن // 2] * 1.0
  # apl-source:22
  return (ق[ن // 2 - 1] + ق[ن // 2]) / 2
# apl-source:23

# apl-source:24
def وسطاء_النوافذ(أ, ك):
  # apl-source:25
  ناتج = []
  # apl-source:26
  for ع in range(len(أ) - ك + 1):
    # apl-source:27
    ناتج = ناتج + [وسيط(sorted(أ[ع:ع + ك]))]
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(وسطاء_النوافذ([1,3,-1,-3,5,3,6,7], 3), [1.0,-1.0,-1.0,3.0,5.0,6.0], "مثال أول")
# apl-source:31
تأكد_يساوي(وسطاء_النوافذ([1,2,3,4], 2), [1.5,2.5,3.5], "زوجي")
# apl-source:32
تأكد_يساوي(وسطاء_النوافذ([5], 1), [5.0], "عنصر")
# apl-source:33
