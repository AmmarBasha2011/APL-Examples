
# apl-source:1
# مثال 1094 — تعطيل عنوان IP
# apl-source:2
# Defanging an IP address
# apl-source:3
# Demonstrates: استبدال حرف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1094-defang-ip.apl
# apl-source:6

# apl-source:7
# نكتب كل نقطة في عنوان IP بين قوسين مربعين
# apl-source:8
# حتى لا يتحول لرابط قابل للنقر
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
def عطّل(عنوان):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  for ح in عنوان:
    # apl-source:21
    if ح == ".":
      # apl-source:22
      ناتج = ناتج + "[.]"
    # apl-source:23
    else:
      # apl-source:24
      ناتج = ناتج + ح
  # apl-source:25
  return ناتج
# apl-source:26

# apl-source:27
تأكد_يساوي(عطّل("1.1.1.1"), "1[.]1[.]1[.]1", "أربع نقاط")
# apl-source:28
تأكد_يساوي(عطّل("255.100.50.0"), "255[.]100[.]50[.]0", "عنوان آخر")
# apl-source:29
تأكد_يساوي(عطّل("abc"), "abc", "بلا نقاط")
# apl-source:30
