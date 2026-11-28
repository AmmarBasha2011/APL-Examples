
# apl-source:1
# مثال 1659 — جذر العدد الأولي
# apl-source:2
# Radical of an integer
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1659-radical-of-number.apl
# apl-source:6

# apl-source:7
# نحلل العدد
# apl-source:8
# نضرب كل عامل مرة واحدة فقط
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
def الجذر_الأولي(ن):
  # apl-source:19
  حاصل = 1
  # apl-source:20
  ك = 2
  # apl-source:21
  while ك * ك <= ن:
    # apl-source:22
    if ن % ك == 0:
      # apl-source:23
      حاصل = حاصل * ك
      # apl-source:24
      while ن % ك == 0:
        # apl-source:25
        ن = ن // ك
    # apl-source:26
    ك = ك + 1
  # apl-source:27
  if ن > 1:
    # apl-source:28
    حاصل = حاصل * ن
  # apl-source:29
  return حاصل
# apl-source:30

# apl-source:31
تأكد_يساوي(الجذر_الأولي(12), 6, "اثنا عشر")
# apl-source:32
تأكد_يساوي(الجذر_الأولي(7), 7, "أولي")
# apl-source:33
تأكد_يساوي(الجذر_الأولي(1000), 10, "ألف")
# apl-source:34
تأكد_يساوي(الجذر_الأولي(1), 1, "واحد")
# apl-source:35
