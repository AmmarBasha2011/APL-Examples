
# apl-source:1
# مثال 1691 — شيفرة غراي
# apl-source:2
# Gray code sequence
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1691-gray-code-sequence.apl
# apl-source:6

# apl-source:7
# غراي(ن) = ن ^ (ن >> 1)
# apl-source:8
# نولد التسلسل كاملاً
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
def غراي(ن):
  # apl-source:19
  return ن ^ (ن >> 1)
# apl-source:20

# apl-source:21
def تسلسل_غراي(بتات):
  # apl-source:22
  ناتج = []
  # apl-source:23
  for ع in range(2 ** بتات):
    # apl-source:24
    ناتج.append(غراي(ع))
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(تسلسل_غراي(2), [0, 1, 3, 2], "بتان")
# apl-source:28
تأكد_يساوي(تسلسل_غراي(3), [0, 1, 3, 2, 6, 7, 5, 4], "ثلاثة")
# apl-source:29
