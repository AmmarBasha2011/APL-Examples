
# apl-source:1
# مثال 1305 — حذف العقدة من النهاية
# apl-source:2
# Remove nth node from end
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1305-remove-nth-from-end.apl
# apl-source:6

# apl-source:7
# مؤشر يتقدم n خطوة أولاً
# apl-source:8
# ثم يمشي المؤشران معاً حتى النهاية
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
  ق = list(قيم)
  # apl-source:20
  سريع = 0
  # apl-source:21
  for ع in range(ن):
    # apl-source:22
    سريع = سريع + 1
  # apl-source:23
  بطيء = 0
  # apl-source:24
  while سريع < len(ق):
    # apl-source:25
    سريع = سريع + 1
    # apl-source:26
    بطيء = بطيء + 1
  # apl-source:27
  ق.pop(بطيء)
  # apl-source:28
  return ق
# apl-source:29

# apl-source:30
تأكد_يساوي(احذف_من_النهاية([1,2,3,4,5], 2), [1,2,3,5], "الثاني من النهاية")
# apl-source:31
تأكد_يساوي(احذف_من_النهاية([1], 1), [], "الوحيد")
# apl-source:32
تأكد_يساوي(احذف_من_النهاية([1,2], 1), [1], "الأخير")
# apl-source:33
تأكد_يساوي(احذف_من_النهاية([1,2], 2), [2], "الأول")
# apl-source:34
