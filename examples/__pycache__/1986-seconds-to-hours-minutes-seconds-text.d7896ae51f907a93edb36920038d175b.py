
# apl-source:1
# مثال 1986 — تحويل الثواني إلى ساعات ودقائق وثوان
# apl-source:2
# Seconds to H:MM:SS
# apl-source:3
# Demonstrates: تواريخ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1986-seconds-to-hours-minutes-seconds-text.apl
# apl-source:6

# apl-source:7
# # الدقائق والثواني تأخذ خانتين
# apl-source:8
# # والساعات تكتب كما هي
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
def نسق(ث):
  # apl-source:19
  س = ث // 3600
  # apl-source:20
  م = (ث % 3600) // 60
  # apl-source:21
  ن = ث % 60
  # apl-source:22
  return str(س) + ":" + str(م).zfill(2) + ":" + str(ن).zfill(2)
# apl-source:23

# apl-source:24
تأكد_يساوي(نسق(3725), "1:02:05", "عادي")
# apl-source:25
تأكد_يساوي(نسق(59), "0:00:59", "ثوان")
# apl-source:26
تأكد_يساوي(نسق(86400), "24:00:00", "يوم")
# apl-source:27
تأكد_يساوي(نسق(0), "0:00:00", "صفر")
# apl-source:28
