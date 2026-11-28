import time
# apl-source:1
# مثال 1426 — أقرب وقت تالٍ
# apl-source:2
# Next closest time reusing digits
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1426-next-closest-time.apl
# apl-source:6

# apl-source:7
# نتقدم دقيقة دقيقة
# apl-source:8
# ونقبل أول وقت أرقامه كلها من الأرقام الأصلية
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
def بخانتين(ن):
  # apl-source:19
  if ن < 10:
    # apl-source:20
    return "0" + str(ن)
  # apl-source:21
  return str(ن)
# apl-source:22

# apl-source:23
def وقت_تالي(وقت):
  # apl-source:24
  مسموح = {}
  # apl-source:25
  for ح in وقت:
    # apl-source:26
    مسموح[ح] = True
  # apl-source:27
  قيمة_الوقت = int(وقت[:2]) * 60 + int(وقت[3:])
  # apl-source:28
  for خطوة in range(1, 1441):
    # apl-source:29
    ت = (قيمة_الوقت + خطوة) % 1440
    # apl-source:30
    نتيجة = بخانتين(ت // 60) + ":" + بخانتين(ت % 60)
    # apl-source:31
    سليم = True
    # apl-source:32
    for ح in نتيجة:
      # apl-source:33
      if ح not in مسموح:
        # apl-source:34
        سليم = False
    # apl-source:35
    if سليم:
      # apl-source:36
      return نتيجة
  # apl-source:37
  return وقت
# apl-source:38

# apl-source:39
تأكد_يساوي(وقت_تالي("19:34"), "19:39", "مثال أول")
# apl-source:40
تأكد_يساوي(وقت_تالي("23:59"), "22:22", "منتصف الليل")
# apl-source:41
تأكد_يساوي(وقت_تالي("01:32"), "01:33", "دقيقة")
# apl-source:42
