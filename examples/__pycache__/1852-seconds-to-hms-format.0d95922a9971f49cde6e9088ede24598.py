
# apl-source:1
# مثال 1852 — من الثواني إلى ساعات ودقائق
# apl-source:2
# Seconds to hours minutes seconds
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1852-seconds-to-hms-format.apl
# apl-source:6

# apl-source:7
# نحسب الساعات أولاً
# apl-source:8
# نحشو الأصفار على اليسار
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
def حشو(ن):
  # apl-source:19
  if ن < 10:
    # apl-source:20
    return "0" + str(ن)
  # apl-source:21
  return str(ن)
# apl-source:22

# apl-source:23
def تنسيق(ثواني):
  # apl-source:24
  س = ثواني // 3600
  # apl-source:25
  د = (ثواني % 3600) // 60
  # apl-source:26
  ث = ثواني % 60
  # apl-source:27
  return حشو(س) + ":" + حشو(د) + ":" + حشو(ث)
# apl-source:28

# apl-source:29
تأكد_يساوي(تنسيق(3661), "01:01:01", "ساعة ودقيقة وثانية")
# apl-source:30
تأكد_يساوي(تنسيق(59), "00:00:59", "ثواني")
# apl-source:31
تأكد_يساوي(تنسيق(86399), "23:59:59", "آخر اليوم")
# apl-source:32
