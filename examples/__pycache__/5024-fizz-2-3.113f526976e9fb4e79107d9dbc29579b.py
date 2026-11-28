
# apl-source:1
# مثال 5024 — فيزباز بالعددين 2 و 3
# apl-source:2
# FizzBuzz variant with 2 and 3
# apl-source:3
# Demonstrates: منطق وتمارين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/5024-fizz-2-3.apl
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
    if ي % 2 == 0 and ي % 3 == 0:
      # apl-source:21
      ر = ر + ["AB"]
    # apl-source:22
    elif ي % 2 == 0:
      # apl-source:23
      ر = ر + ["A"]
    # apl-source:24
    elif ي % 3 == 0:
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
تأكد_يساوي(ف(10), ["1", "A", "B", "A", "5", "AB", "7", "A", "B", "A"], "حالة 2")
# apl-source:32
تأكد_يساوي(ف(30), ["1", "A", "B", "A", "5", "AB", "7", "A", "B", "A", "11", "AB", "13", "A", "B", "A", "17", "AB", "19", "A", "B", "A", "23", "AB", "25", "A", "B", "A", "29", "AB"], "حالة 3")
# apl-source:33
تأكد_يساوي(ف(0), [], "حالة 4")
# apl-source:34
