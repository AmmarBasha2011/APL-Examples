
# apl-source:1
# مثال 1493 — تحليل نص الوقت
# apl-source:2
# Parse HH:MM time string
# apl-source:3
# Demonstrates: تحليل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1493-time-string-parse.apl
# apl-source:6

# apl-source:7
# نفصل على النقطتين
# apl-source:8
# الساعة من 0 إلى 23 والدقيقة من 0 إلى 59
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
def دقائق_اليوم(نص_):
  # apl-source:19
  أجزاء = نص_.split(":")
  # apl-source:20
  if len(أجزاء) != 2:
    # apl-source:21
    return -1
  # apl-source:22
  if أجزاء[0].isdigit() == False or أجزاء[1].isdigit() == False:
    # apl-source:23
    return -1
  # apl-source:24
  س = int(أجزاء[0])
  # apl-source:25
  د = int(أجزاء[1])
  # apl-source:26
  if س > 23 or د > 59:
    # apl-source:27
    return -1
  # apl-source:28
  return س * 60 + د
# apl-source:29

# apl-source:30
تأكد_يساوي(دقائق_اليوم("14:30"), 870, "ظهراً")
# apl-source:31
تأكد_يساوي(دقائق_اليوم("00:00"), 0, "منتصف الليل")
# apl-source:32
تأكد_يساوي(دقائق_اليوم("24:00"), -1, "ساعة خاطئة")
# apl-source:33
تأكد_يساوي(دقائق_اليوم("12-30"), -1, "صيغة خاطئة")
# apl-source:34
