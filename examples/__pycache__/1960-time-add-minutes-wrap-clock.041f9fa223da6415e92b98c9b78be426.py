
# apl-source:1
# مثال 1960 — إضافة دقائق إلى ساعة بصيغة HH:MM
# apl-source:2
# Add minutes to clock time
# apl-source:3
# Demonstrates: تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1960-time-add-minutes-wrap-clock.apl
# apl-source:6

# apl-source:7
# # نفك النص إلى ساعة ودقيقة
# apl-source:8
# # ونلف حول منتصف الليل
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
def اضف(وقت, د):
  # apl-source:19
  اجزاء = وقت.split(":")
  # apl-source:20
  كلي = (int(اجزاء[0]) * 60 + int(اجزاء[1]) + د) % 1440
  # apl-source:21
  س = كلي // 60
  # apl-source:22
  م = كلي % 60
  # apl-source:23
  if س < 10:
    # apl-source:24
    ن_س = "0" + str(س)
  # apl-source:25
  else:
    # apl-source:26
    ن_س = str(س)
  # apl-source:27
  if م < 10:
    # apl-source:28
    ن_م = "0" + str(م)
  # apl-source:29
  else:
    # apl-source:30
    ن_م = str(م)
  # apl-source:31
  return ن_س + ":" + ن_م
# apl-source:32

# apl-source:33
تأكد_يساوي(اضف("09:30", 45), "10:15", "عادي")
# apl-source:34
تأكد_يساوي(اضف("23:50", 20), "00:10", "منتصف الليل")
# apl-source:35
تأكد_يساوي(اضف("00:00", 1440), "00:00", "يوم كامل")
# apl-source:36
تأكد_يساوي(اضف("12:05", -10), "11:55", "طرح")
# apl-source:37
