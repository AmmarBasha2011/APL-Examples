
# apl-source:1
# مثال 5025 — فيزباز بالعددين 4 و 9
# apl-source:2
# FizzBuzz variant with 4 and 9
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5025-fizz-4-9.apl
# apl-source:6

# apl-source:7
# A للقابل على الأول، B للثاني، AB للاثنين
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
  for ي in range(1, ن + 1):
    # apl-source:20
    if ي % 4 == 0 and ي % 9 == 0:
      # apl-source:21
      ر = ر + ["AB"]
    # apl-source:22
    elif ي % 4 == 0:
      # apl-source:23
      ر = ر + ["A"]
    # apl-source:24
    elif ي % 9 == 0:
      # apl-source:25
      ر = ر + ["B"]
    # apl-source:26
    else:
      # apl-source:27
      ر = ر + [str(ي)]
  # apl-source:28
  return ر
# apl-source:29

# apl-source:30
تأكد_يساوي(ف(1), ["1"], "حالة 1")
# apl-source:31
تأكد_يساوي(ف(10), ["1", "2", "3", "A", "5", "6", "7", "A", "B", "10"], "حالة 2")
# apl-source:32
تأكد_يساوي(ف(30), ["1", "2", "3", "A", "5", "6", "7", "A", "B", "10", "11", "A", "13", "14", "15", "A", "17", "B", "19", "A", "21", "22", "23", "A", "25", "26", "B", "A", "29", "30"], "حالة 3")
# apl-source:33
تأكد_يساوي(ف(0), [], "حالة 4")
# apl-source:34
