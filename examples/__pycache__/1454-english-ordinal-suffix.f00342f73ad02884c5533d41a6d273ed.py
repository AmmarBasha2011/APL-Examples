
# apl-source:1
# مثال 1454 — لاحقة الترتيب بالإنجليزية
# apl-source:2
# English ordinal suffix
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1454-english-ordinal-suffix.apl
# apl-source:6

# apl-source:7
# الأرقام من 11 إلى 13 تأخذ th
# apl-source:8
# وإلا ننظر لآخر رقم
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
def ترتيبي(ن):
  # apl-source:19
  باقي = ن % 100
  # apl-source:20
  if باقي >= 11 and باقي <= 13:
    # apl-source:21
    return str(ن) + "th"
  # apl-source:22
  آخر = ن % 10
  # apl-source:23
  if آخر == 1:
    # apl-source:24
    return str(ن) + "st"
  # apl-source:25
  elif آخر == 2:
    # apl-source:26
    return str(ن) + "nd"
  # apl-source:27
  elif آخر == 3:
    # apl-source:28
    return str(ن) + "rd"
  # apl-source:29
  return str(ن) + "th"
# apl-source:30

# apl-source:31
تأكد_يساوي(ترتيبي(1), "1st", "أول")
# apl-source:32
تأكد_يساوي(ترتيبي(22), "22nd", "اثنان وعشرون")
# apl-source:33
تأكد_يساوي(ترتيبي(113), "113th", "استثناء")
# apl-source:34
تأكد_يساوي(ترتيبي(101), "101st", "مئة وواحد")
# apl-source:35
