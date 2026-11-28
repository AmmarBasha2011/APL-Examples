
# apl-source:1
# مثال 1095 — هل يعود الروبوت
# apl-source:2
# Robot return to origin
# apl-source:3
# Demonstrates: إحداثيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1095-route-circle.apl
# apl-source:6

# apl-source:7
# U وD تغيران المحور الرأسي وL وR الأفقي
# apl-source:8
# يعود الروبوت لو انتهى عند الصفر في المحورين
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
def يعود(حركات):
  # apl-source:19
  س = 0
  # apl-source:20
  ص = 0
  # apl-source:21
  for ح in حركات:
    # apl-source:22
    if ح == "U":
      # apl-source:23
      ص = ص + 1
    # apl-source:24
    elif ح == "D":
      # apl-source:25
      ص = ص - 1
    # apl-source:26
    elif ح == "L":
      # apl-source:27
      س = س - 1
    # apl-source:28
    elif ح == "R":
      # apl-source:29
      س = س + 1
  # apl-source:30
  return (س == 0) and (ص == 0)
# apl-source:31

# apl-source:32
تأكد_يساوي(يعود("UD"), True, "أعلى وأسفل")
# apl-source:33
تأكد_يساوي(يعود("LL"), False, "يسار مرتين")
# apl-source:34
تأكد_يساوي(يعود("RRDDLUUL"), True, "مسار طويل")
# apl-source:35
تأكد_يساوي(يعود(""), True, "بلا حركات")
# apl-source:36
