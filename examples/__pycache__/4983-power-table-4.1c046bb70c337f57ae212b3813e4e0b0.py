
# apl-source:1
# مثال 4983 — قوى العدد 4 حتى 6
# apl-source:2
# Powers of 4 up to 6
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4983-power-table-4.apl
# apl-source:6

# apl-source:7
# نضرب في العدد في كل خطوة
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ن):
  # apl-source:18
  ر = []
  # apl-source:19
  ق = 1
  # apl-source:20
  for ي in range(ن + 1):
    # apl-source:21
    ر = ر + [ق]
    # apl-source:22
    ق = ق * 4
  # apl-source:23
  return ر
# apl-source:24

# apl-source:25
تأكد_يساوي(ف(0), [1], "حالة 1")
# apl-source:26
تأكد_يساوي(ف(3), [1, 4, 16, 64], "حالة 2")
# apl-source:27
تأكد_يساوي(ف(6), [1, 4, 16, 64, 256, 1024, 4096], "حالة 3")
# apl-source:28
