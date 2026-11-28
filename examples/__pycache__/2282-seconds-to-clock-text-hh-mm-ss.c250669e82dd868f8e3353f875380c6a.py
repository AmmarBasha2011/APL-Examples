
# apl-source:1
# مثال 2282 — ثوان إلى ساعة:دقيقة:ثانية
# apl-source:2
# Seconds to hh:mm:ss
# apl-source:3
# Demonstrates: أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2282-seconds-to-clock-text-hh-mm-ss.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ن):
  # apl-source:19
  س = ن // 3600
  # apl-source:20
  د = (ن % 3600) // 60
  # apl-source:21
  ث = ن % 60
  # apl-source:22
  return str(س).zfill(2) + ":" + str(د).zfill(2) + ":" + str(ث).zfill(2)
# apl-source:23

# apl-source:24
تأكد_يساوي(ف(0), "00:00:00", "حالة 1")
# apl-source:25
تأكد_يساوي(ف(59), "00:00:59", "حالة 2")
# apl-source:26
تأكد_يساوي(ف(60), "00:01:00", "حالة 3")
# apl-source:27
تأكد_يساوي(ف(3661), "01:01:01", "حالة 4")
# apl-source:28
تأكد_يساوي(ف(86399), "23:59:59", "حالة 5")
# apl-source:29
