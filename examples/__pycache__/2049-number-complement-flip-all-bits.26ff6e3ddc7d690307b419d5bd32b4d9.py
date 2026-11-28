
# apl-source:1
# مثال 2049 — متمم العدد بقلب كل بتاته
# apl-source:2
# Number complement
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2049-number-complement-flip-all-bits.apl
# apl-source:6

# apl-source:7
# # القناع يساوي 2 أس طول العدد ناقص 1
# apl-source:8
# # XOR مع القناع يقلب البتات
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
  م = 1
  # apl-source:20
  while م <= ن:
    # apl-source:21
    م = م << 1
  # apl-source:22
  return ن ^ (م - 1)
# apl-source:23

# apl-source:24
تأكد_يساوي(متمم(5), 2, "٥")
# apl-source:25
تأكد_يساوي(متمم(1), 0, "١")
# apl-source:26
تأكد_يساوي(متمم(10), 5, "١٠")
# apl-source:27
