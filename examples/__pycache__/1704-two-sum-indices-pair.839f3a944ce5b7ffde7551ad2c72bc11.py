
# apl-source:1
# مثال 1704 — مؤشرا مجموع الهدف
# apl-source:2
# Two sum indices
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1704-two-sum-indices-pair.apl
# apl-source:6

# apl-source:7
# نخزن القيم التي رأيناها
# apl-source:8
# نسأل عن الهدف ناقص القيمة
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
def مؤشرا_المجموع(ق, هدف):
  # apl-source:19
  رأينا = {}
  # apl-source:20
  for ك in range(len(ق)):
    # apl-source:21
    مكمل = هدف - ق[ك]
    # apl-source:22
    if str(مكمل) in رأينا:
      # apl-source:23
      return [رأينا[str(مكمل)], ك]
    # apl-source:24
    رأينا[str(ق[ك])] = ك
  # apl-source:25
  return []
# apl-source:26

# apl-source:27
تأكد_يساوي(مؤشرا_المجموع([2, 7, 11, 15], 9), [0, 1], "أول")
# apl-source:28
تأكد_يساوي(مؤشرا_المجموع([3, 2, 4], 6), [1, 2], "وسط")
# apl-source:29
تأكد_يساوي(مؤشرا_المجموع([1, 2], 10), [], "لا يوجد")
# apl-source:30
