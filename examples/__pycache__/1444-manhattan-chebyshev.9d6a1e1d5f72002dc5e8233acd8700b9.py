
# apl-source:1
# مثال 1444 — مسافة مانهاتن وتشيبيشيف
# apl-source:2
# Manhattan and Chebyshev distance
# apl-source:3
# Demonstrates: هندسة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1444-manhattan-chebyshev.apl
# apl-source:6

# apl-source:7
# مانهاتن مجموع الفروقين المطلقين
# apl-source:8
# تشيبيشيف أكبر الفرقين
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
def مطلقة(س):
  # apl-source:19
  if س < 0:
    # apl-source:20
    return -س
  # apl-source:21
  return س
# apl-source:22

# apl-source:23
def مسافتان(أ, ب):
  # apl-source:24
  فس = مطلقة(أ[0] - ب[0])
  # apl-source:25
  فص = مطلقة(أ[1] - ب[1])
  # apl-source:26
  return [فس + فص, max(فس, فص)]
# apl-source:27

# apl-source:28
تأكد_يساوي(مسافتان([1,2], [4,6]), [7, 4], "مثال أول")
# apl-source:29
تأكد_يساوي(مسافتان([0,0], [0,0]), [0, 0], "نفس النقطة")
# apl-source:30
تأكد_يساوي(مسافتان([-3,-3], [3,3]), [12, 6], "سالبة")
# apl-source:31
