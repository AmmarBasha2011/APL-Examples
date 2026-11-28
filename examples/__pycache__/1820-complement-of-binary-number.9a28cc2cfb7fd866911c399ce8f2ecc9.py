
# apl-source:1
# مثال 1820 — المتمم الثنائي للعدد
# apl-source:2
# Binary complement of number
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1820-complement-of-binary-number.apl
# apl-source:6

# apl-source:7
# نبني قناعاً بطول العدد
# apl-source:8
# نطبق XOR
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
def متمم(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return 1
  # apl-source:21
  قناع = 0
  # apl-source:22
  ك = ن
  # apl-source:23
  while ك > 0:
    # apl-source:24
    قناع = (قناع << 1) | 1
    # apl-source:25
    ك = ك >> 1
  # apl-source:26
  return ن ^ قناع
# apl-source:27

# apl-source:28
تأكد_يساوي(متمم(5), 2, "101")
# apl-source:29
تأكد_يساوي(متمم(1), 0, "واحد")
# apl-source:30
تأكد_يساوي(متمم(10), 5, "1010")
# apl-source:31
