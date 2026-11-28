
# apl-source:1
# مثال 1458 — تقسيم سطر CSV
# apl-source:2
# Split a CSV line with quotes
# apl-source:3
# Demonstrates: تحليل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1458-csv-line-split.apl
# apl-source:6

# apl-source:7
# الفاصلة داخل الاقتباس جزء من الحقل
# apl-source:8
# نقرأ حرفاً حرفاً مع علم للاقتباس
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
def قسّم_سطر(سطر):
  # apl-source:19
  حقول = []
  # apl-source:20
  حقل = ""
  # apl-source:21
  داخل = False
  # apl-source:22
  for ح in سطر:
    # apl-source:23
    if ح == '"':
      # apl-source:24
      داخل = داخل == False
    # apl-source:25
    elif ح == "," and داخل == False:
      # apl-source:26
      حقول.append(حقل)
      # apl-source:27
      حقل = ""
    # apl-source:28
    else:
      # apl-source:29
      حقل = حقل + ح
  # apl-source:30
  حقول.append(حقل)
  # apl-source:31
  return حقول
# apl-source:32

# apl-source:33
تأكد_يساوي(قسّم_سطر("a,b,c"), ["a", "b", "c"], "بسيط")
# apl-source:34
تأكد_يساوي(قسّم_سطر('x,"y,z",w'), ["x", "y,z", "w"], "اقتباس")
# apl-source:35
تأكد_يساوي(قسّم_سطر("a,,c"), ["a", "", "c"], "حقل فارغ")
# apl-source:36
