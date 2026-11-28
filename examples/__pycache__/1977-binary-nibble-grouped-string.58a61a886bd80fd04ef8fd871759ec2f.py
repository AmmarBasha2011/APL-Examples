
# apl-source:1
# مثال 1977 — تقسيم الأعداد الثنائية إلى مجموعات من أربع خانات
# apl-source:2
# Binary grouped in nibbles
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1977-binary-nibble-grouped-string.apl
# apl-source:6

# apl-source:7
# # نبني النص الثنائي بالقسمة على 2
# apl-source:8
# # ثم نملأ من اليسار ونقسم
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
def ثنائي_مجمع(ن):
  # apl-source:19
  س = ""
  # apl-source:20
  if ن == 0:
    # apl-source:21
    س = "0"
  # apl-source:22
  while ن > 0:
    # apl-source:23
    س = str(ن % 2) + س
    # apl-source:24
    ن = ن // 2
  # apl-source:25
  while len(س) % 4 != 0:
    # apl-source:26
    س = "0" + س
  # apl-source:27
  اجزاء = []
  # apl-source:28
  for ك in range(0, len(س), 4):
    # apl-source:29
    اجزاء = اجزاء + [س[ك:ك + 4]]
  # apl-source:30
  return "_".join(اجزاء)
# apl-source:31

# apl-source:32
تأكد_يساوي(ثنائي_مجمع(5), "0101", "٥")
# apl-source:33
تأكد_يساوي(ثنائي_مجمع(255), "1111_1111", "٢٥٥")
# apl-source:34
تأكد_يساوي(ثنائي_مجمع(1000), "0011_1110_1000", "١٠٠٠")
# apl-source:35
تأكد_يساوي(ثنائي_مجمع(0), "0000", "صفر")
# apl-source:36
