
# apl-source:1
# مثال 1685 — عدد المجموعات الجزئية بمجموع معين
# apl-source:2
# Count subsets with target sum
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1685-subsets-with-target-sum-count.apl
# apl-source:6

# apl-source:7
# الجدول يعد الطرق لكل مجموع
# apl-source:8
# نحدث من الأكبر للأصغر
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
def عد_مجموعات(ق, هدف):
  # apl-source:19
  طرق = [1]
  # apl-source:20
  for ك in range(هدف):
    # apl-source:21
    طرق.append(0)
  # apl-source:22
  for ع in ق:
    # apl-source:23
    ن = هدف
    # apl-source:24
    while ن >= ع:
      # apl-source:25
      طرق[ن] = طرق[ن] + طرق[ن - ع]
      # apl-source:26
      ن = ن - 1
  # apl-source:27
  return طرق[هدف]
# apl-source:28

# apl-source:29
تأكد_يساوي(عد_مجموعات([1, 2, 3, 4, 5], 5), 3, "خمسة")
# apl-source:30
تأكد_يساوي(عد_مجموعات([1, 1, 1], 2), 3, "مكررة")
# apl-source:31
تأكد_يساوي(عد_مجموعات([2, 4], 3), 0, "مستحيل")
# apl-source:32
