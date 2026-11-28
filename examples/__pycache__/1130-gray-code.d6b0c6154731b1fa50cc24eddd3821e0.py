
# apl-source:1
# مثال 1130 — شيفرة غراي
# apl-source:2
# Gray code sequence
# apl-source:3
# Demonstrates: تحويل ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1130-gray-code.apl
# apl-source:6

# apl-source:7
# الرقم ن يُحوَّل بإزاحة بت وعملية XOR
# apl-source:8
# فيختلف كل رقمين متجاورين ببت واحد
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
  ناتج = []
  # apl-source:20
  for ع in range(2 ** ن):
    # apl-source:21
    ناتج = ناتج + [ع ^ (ع >> 1)]
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
def بتات_مختلفة(أ, ب):
  # apl-source:25
  س = أ ^ ب
  # apl-source:26
  ع = 0
  # apl-source:27
  while س > 0:
    # apl-source:28
    ع = ع + (س & 1)
    # apl-source:29
    س = س >> 1
  # apl-source:30
  return ع
# apl-source:31

# apl-source:32
تأكد_يساوي(غراي(1), [0, 1], "بت")
# apl-source:33
تأكد_يساوي(غراي(2), [0, 1, 3, 2], "بتان")
# apl-source:34
تأكد_يساوي(غراي(3), [0, 1, 3, 2, 6, 7, 5, 4], "ثلاثة")
# apl-source:35
ق = غراي(4)
# apl-source:36
سليم = True
# apl-source:37
for ع in range(len(ق) - 1):
  # apl-source:38
  if بتات_مختلفة(ق[ع], ق[ع + 1]) != 1:
    # apl-source:39
    سليم = False
# apl-source:40
تأكد_يساوي(سليم, True, "فرق بت واحد")
# apl-source:41
