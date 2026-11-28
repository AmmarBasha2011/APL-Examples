
# apl-source:1
# مثال 1463 — من الثواني إلى ساعة:دقيقة:ثانية
# apl-source:2
# Seconds to hh:mm:ss
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1463-seconds-to-clock.apl
# apl-source:6

# apl-source:7
# نقسم على 3600 ثم 60
# apl-source:8
# نضيف صفراً لكل رقم أقل من عشرة
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
def رقمين(ن):
  # apl-source:19
  if ن < 10:
    # apl-source:20
    return "0" + str(ن)
  # apl-source:21
  return str(ن)
# apl-source:22

# apl-source:23
def كساعة(ث):
  # apl-source:24
  س = ث // 3600
  # apl-source:25
  د = (ث % 3600) // 60
  # apl-source:26
  ثا = ث % 60
  # apl-source:27
  return رقمين(س) + ":" + رقمين(د) + ":" + رقمين(ثا)
# apl-source:28

# apl-source:29
تأكد_يساوي(كساعة(0), "00:00:00", "صفر")
# apl-source:30
تأكد_يساوي(كساعة(3661), "01:01:01", "ساعة ودقيقة وثانية")
# apl-source:31
تأكد_يساوي(كساعة(86399), "23:59:59", "آخر اليوم")
# apl-source:32
