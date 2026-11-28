
# apl-source:1
# مثال 1079 — متمم العدد
# apl-source:2
# Number complement
# apl-source:3
# Demonstrates: قناع بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1079-number-complement.apl
# apl-source:6

# apl-source:7
# نبني قناعاً من آحاد بطول العدد الثنائي
# apl-source:8
# XOR مع القناع يقلب كل بت
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
  قناع = 1
  # apl-source:20
  while قناع <= ن:
    # apl-source:21
    قناع = قناع * 2
  # apl-source:22
  return (قناع - 1) ^ ن
# apl-source:23

# apl-source:24
تأكد_يساوي(متمم(5), 2, "101 إلى 010")
# apl-source:25
تأكد_يساوي(متمم(1), 0, "واحد")
# apl-source:26
تأكد_يساوي(متمم(10), 5, "1010 إلى 0101")
# apl-source:27
تأكد_يساوي(متمم(255), 0, "كلها آحاد")
# apl-source:28
