
# apl-source:1
# مثال 1390 — مجموع المضاعفات
# apl-source:2
# Sum of multiples below limit
# apl-source:3
# Demonstrates: رياضيات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1390-sum-of-multiples-below.apl
# apl-source:6

# apl-source:7
# نجمع كل عدد يقبل القسمة على أحدهما
# apl-source:8
# ويمكن أيضاً بالصيغة المغلقة
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
def مجموع_مضاعفات(حد):
  # apl-source:19
  م = 0
  # apl-source:20
  for ن in range(1, حد):
    # apl-source:21
    if (ن % 3 == 0) or (ن % 5 == 0):
      # apl-source:22
      م = م + ن
  # apl-source:23
  return م
# apl-source:24

# apl-source:25
def حسابي(حد, ك):
  # apl-source:26
  ع = (حد - 1) // ك
  # apl-source:27
  return ك * ع * (ع + 1) // 2
# apl-source:28

# apl-source:29
def مجموع_مغلق(حد):
  # apl-source:30
  return حسابي(حد, 3) + حسابي(حد, 5) - حسابي(حد, 15)
# apl-source:31

# apl-source:32
تأكد_يساوي(مجموع_مضاعفات(10), 23, "عشرة")
# apl-source:33
تأكد_يساوي(مجموع_مضاعفات(1000), 233168, "ألف")
# apl-source:34
تأكد_يساوي(مجموع_مغلق(1000), 233168, "صيغة مغلقة")
# apl-source:35
تأكد_يساوي(مجموع_مضاعفات(1), 0, "واحد")
# apl-source:36
