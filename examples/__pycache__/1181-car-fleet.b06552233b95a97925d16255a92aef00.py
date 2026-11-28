
# apl-source:1
# مثال 1181 — أساطيل السيارات
# apl-source:2
# Car fleet
# apl-source:3
# Demonstrates: ترتيب بالمسافة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1181-car-fleet.apl
# apl-source:6

# apl-source:7
# نرتب السيارات من الأقرب للهدف
# apl-source:8
# ومن تصل بعد السابقة تشكل أسطولاً جديداً
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
def اساطيل(هدف, مواقع, سرعات):
  # apl-source:19
  ازواج = []
  # apl-source:20
  for ع in range(len(مواقع)):
    # apl-source:21
    ازواج = ازواج + [[مواقع[ع], سرعات[ع]]]
  # apl-source:22
  ازواج = sorted(ازواج)
  # apl-source:23
  ازواج.reverse()
  # apl-source:24
  عدد_ = 0
  # apl-source:25
  اخر_وقت = 0.0
  # apl-source:26
  for ز in ازواج:
    # apl-source:27
    وقت = (هدف - ز[0]) / ز[1]
    # apl-source:28
    if وقت > اخر_وقت:
      # apl-source:29
      عدد_ = عدد_ + 1
      # apl-source:30
      اخر_وقت = وقت
  # apl-source:31
  return عدد_
# apl-source:32

# apl-source:33
تأكد_يساوي(اساطيل(12, [10,8,0,5,3], [2,4,1,1,3]), 3, "مثال أول")
# apl-source:34
تأكد_يساوي(اساطيل(10, [3], [3]), 1, "سيارة واحدة")
# apl-source:35
تأكد_يساوي(اساطيل(100, [0,2,4], [4,2,1]), 1, "كلها تلحق")
# apl-source:36
