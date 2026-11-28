
# apl-source:1
# مثال 1184 — آلة حاسبة بسيطة
# apl-source:2
# Basic calculator with parentheses
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1184-basic-calculator.apl
# apl-source:6

# apl-source:7
# نحتفظ بالعلامة والنتيجة عند كل قوس
# apl-source:8
# ونستعيدهما عند الإغلاق
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
def احسب(س):
  # apl-source:19
  مكدس = []
  # apl-source:20
  نتيجة = 0
  # apl-source:21
  رقم = 0
  # apl-source:22
  علامة = 1
  # apl-source:23
  for ح in س:
    # apl-source:24
    if ح.isdigit():
      # apl-source:25
      رقم = رقم * 10 + int(ح)
    # apl-source:26
    elif (ح == "+") or (ح == "-"):
      # apl-source:27
      نتيجة = نتيجة + علامة * رقم
      # apl-source:28
      رقم = 0
      # apl-source:29
      if ح == "+":
        # apl-source:30
        علامة = 1
      # apl-source:31
      else:
        # apl-source:32
        علامة = -1
    # apl-source:33
    elif ح == "(":
      # apl-source:34
      مكدس = مكدس + [نتيجة]
      # apl-source:35
      مكدس = مكدس + [علامة]
      # apl-source:36
      نتيجة = 0
      # apl-source:37
      علامة = 1
    # apl-source:38
    elif ح == ")":
      # apl-source:39
      نتيجة = نتيجة + علامة * رقم
      # apl-source:40
      رقم = 0
      # apl-source:41
      نتيجة = نتيجة * مكدس.pop() + مكدس.pop()
  # apl-source:42
  return نتيجة + علامة * رقم
# apl-source:43

# apl-source:44
تأكد_يساوي(احسب("1 + 1"), 2, "بسيط")
# apl-source:45
تأكد_يساوي(احسب(" 2-1 + 2 "), 3, "فراغات")
# apl-source:46
تأكد_يساوي(احسب("(1+(4+5+2)-3)+(6+8)"), 23, "أقواس")
# apl-source:47
تأكد_يساوي(احسب("10-(2+3)"), 5, "طرح قوس")
# apl-source:48
تأكد_يساوي(احسب("1-(2-3)"), 2, "علامة معكوسة")
# apl-source:49
