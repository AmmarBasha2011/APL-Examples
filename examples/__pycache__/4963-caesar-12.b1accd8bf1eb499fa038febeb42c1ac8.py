
# apl-source:1
# مثال 4963 — شيفرة قيصر بإزاحة 12
# apl-source:2
# Caesar cipher shift 12
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4963-caesar-12.apl
# apl-source:6

# apl-source:7
# نزيح كل حرف إنجليزي صغير
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
  ر = ""
  # apl-source:19
  for ح in ن:
    # apl-source:20
    if ح >= "a" and ح <= "z":
      # apl-source:21
      ر = ر + chr((ord(ح) - 97 + 12) % 26 + 97)
    # apl-source:22
    else:
      # apl-source:23
      ر = ر + ح
  # apl-source:24
  return ر
# apl-source:25

# apl-source:26
تأكد_يساوي(ف("abc"), "mno", "حالة 1")
# apl-source:27
تأكد_يساوي(ف("hello world"), "tqxxa iadxp", "حالة 2")
# apl-source:28
تأكد_يساوي(ف("xyz"), "jkl", "حالة 3")
# apl-source:29
تأكد_يساوي(ف("a b-c"), "m n-o", "حالة 4")
# apl-source:30
