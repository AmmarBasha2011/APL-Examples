
# apl-source:1
# مثال 1766 — حذف العقدة رقم ن من النهاية
# apl-source:2
# Remove nth node from end
# apl-source:3
# Demonstrates: قوائم مترابطة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1766-linked-list-remove-nth-from-end.apl
# apl-source:6

# apl-source:7
# الموضع من البداية = الطول - ن
# apl-source:8
# نحول المؤشر السابق
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
def احذف_من_النهاية(قيم, ن):
  # apl-source:19
  موضع = len(قيم) - ن
  # apl-source:20
  ناتج = []
  # apl-source:21
  for ك in range(len(قيم)):
    # apl-source:22
    if ك != موضع:
      # apl-source:23
      ناتج.append(قيم[ك])
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
تأكد_يساوي(احذف_من_النهاية([1, 2, 3, 4, 5], 2), [1, 2, 3, 5], "الثاني")
# apl-source:27
تأكد_يساوي(احذف_من_النهاية([1, 2], 2), [2], "الأول")
# apl-source:28
تأكد_يساوي(احذف_من_النهاية([7], 1), [], "الوحيد")
# apl-source:29
