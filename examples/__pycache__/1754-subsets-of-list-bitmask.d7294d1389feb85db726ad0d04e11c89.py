
# apl-source:1
# مثال 1754 — كل المجموعات الجزئية بالقناع
# apl-source:2
# All subsets via bitmask
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1754-subsets-of-list-bitmask.apl
# apl-source:6

# apl-source:7
# نمر على 2^ن قناعاً
# apl-source:8
# البت المضاء يعني اختيار العنصر
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
def مجموعات(ق):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for قناع in range(2 ** len(ق)):
    # apl-source:21
    جزء = []
    # apl-source:22
    for ك in range(len(ق)):
      # apl-source:23
      if (قناع >> ك) & 1 == 1:
        # apl-source:24
        جزء.append(ق[ك])
    # apl-source:25
    ناتج.append(جزء)
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(مجموعات([1, 2]), [[], [1], [2], [1, 2]], "اثنان")
# apl-source:29
تأكد_يساوي(len(مجموعات([1, 2, 3, 4])), 16, "أربعة")
# apl-source:30
تأكد_يساوي(مجموعات([]), [[]], "فارغة")
# apl-source:31
