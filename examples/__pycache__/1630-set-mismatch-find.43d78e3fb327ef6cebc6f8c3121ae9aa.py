
# apl-source:1
# مثال 1630 — المكرر والمفقود
# apl-source:2
# Find duplicate and missing number
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1630-set-mismatch-find.apl
# apl-source:6

# apl-source:7
# نعد كل رقم
# apl-source:8
# المكرر عدّه اثنان والمفقود صفر
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
def خطأ_المجموعة(أ):
  # apl-source:19
  عد = {}
  # apl-source:20
  for ع in أ:
    # apl-source:21
    عد[ع] = عد.get(ع, 0) + 1
  # apl-source:22
  مكرر = -1
  # apl-source:23
  مفقود = -1
  # apl-source:24
  for ك in range(1, len(أ) + 1):
    # apl-source:25
    if عد.get(ك, 0) == 2:
      # apl-source:26
      مكرر = ك
    # apl-source:27
    if عد.get(ك, 0) == 0:
      # apl-source:28
      مفقود = ك
  # apl-source:29
  return [مكرر, مفقود]
# apl-source:30

# apl-source:31
تأكد_يساوي(خطأ_المجموعة([1, 2, 2, 4]), [2, 3], "أربعة")
# apl-source:32
تأكد_يساوي(خطأ_المجموعة([1, 1]), [1, 2], "اثنان")
# apl-source:33
تأكد_يساوي(خطأ_المجموعة([3, 2, 3, 4, 6, 5]), [3, 1], "ستة")
# apl-source:34
