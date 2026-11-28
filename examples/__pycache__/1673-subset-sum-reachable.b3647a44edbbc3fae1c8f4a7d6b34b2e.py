
# apl-source:1
# مثال 1673 — هل يوجد مجموع جزئي
# apl-source:2
# Subset sum reachable
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1673-subset-sum-reachable.apl
# apl-source:6

# apl-source:7
# جدول من الأهداف الممكنة
# apl-source:8
# نمر على العناصر ونحدث الجدول من النهاية
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
def مجموع_ممكن(ق, هدف):
  # apl-source:19
  ممكن = [True]
  # apl-source:20
  for ك in range(هدف):
    # apl-source:21
    ممكن.append(False)
  # apl-source:22
  for ع in ق:
    # apl-source:23
    ن = هدف
    # apl-source:24
    while ن >= ع:
      # apl-source:25
      if ممكن[ن - ع]:
        # apl-source:26
        ممكن[ن] = True
      # apl-source:27
      ن = ن - 1
  # apl-source:28
  return ممكن[هدف]
# apl-source:29

# apl-source:30
تأكد_يساوي(مجموع_ممكن([3, 34, 4, 12, 5, 2], 9), True, "تسعة")
# apl-source:31
تأكد_يساوي(مجموع_ممكن([3, 34, 4, 12, 5, 2], 30), False, "ثلاثون")
# apl-source:32
تأكد_يساوي(مجموع_ممكن([5], 0), True, "صفر")
# apl-source:33
