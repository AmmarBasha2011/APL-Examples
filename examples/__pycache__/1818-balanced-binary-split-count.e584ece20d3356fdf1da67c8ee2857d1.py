
# apl-source:1
# مثال 1818 — عدد الانقسامات المتوازنة
# apl-source:2
# Balanced split count of 0 and 1
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1818-balanced-binary-split-count.apl
# apl-source:6

# apl-source:7
# نعد الفرق التراكمي
# apl-source:8
# كل مرة يعود الفرق صفراً نقسم
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
def انقسامات(س):
  # apl-source:19
  فرق = 0
  # apl-source:20
  عد = 0
  # apl-source:21
  for ح in س:
    # apl-source:22
    if ح == "0":
      # apl-source:23
      فرق = فرق + 1
    # apl-source:24
    else:
      # apl-source:25
      فرق = فرق - 1
    # apl-source:26
    if فرق == 0:
      # apl-source:27
      عد = عد + 1
  # apl-source:28
  return عد
# apl-source:29

# apl-source:30
تأكد_يساوي(انقسامات("010011"), 2, "اثنان")
# apl-source:31
تأكد_يساوي(انقسامات("0101"), 2, "متكرر")
# apl-source:32
تأكد_يساوي(انقسامات("0011"), 1, "واحد")
# apl-source:33
