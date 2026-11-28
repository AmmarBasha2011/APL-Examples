
# apl-source:1
# مثال 1674 — كل السلاسل الثنائية بطول ن
# apl-source:2
# All binary strings of length n
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1674-binary-strings-of-length-n.apl
# apl-source:6

# apl-source:7
# العدد 2 أس ن
# apl-source:8
# نحول كل رقم إلى ثنائي بحشو الأصفار
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
def سلاسل(ن):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in range(2 ** ن):
    # apl-source:21
    س = ""
    # apl-source:22
    ك = ع
    # apl-source:23
    for ي in range(ن):
      # apl-source:24
      س = str(ك % 2) + س
      # apl-source:25
      ك = ك // 2
    # apl-source:26
    ناتج.append(س)
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
تأكد_يساوي(سلاسل(2), ["00", "01", "10", "11"], "اثنان")
# apl-source:30
تأكد_يساوي(len(سلاسل(4)), 16, "أربعة")
# apl-source:31
تأكد_يساوي(سلاسل(1), ["0", "1"], "واحد")
# apl-source:32
