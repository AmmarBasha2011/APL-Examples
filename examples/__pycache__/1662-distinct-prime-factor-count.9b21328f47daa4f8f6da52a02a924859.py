
# apl-source:1
# مثال 1662 — عدد العوامل الأولية المختلفة
# apl-source:2
# Distinct prime factor count
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1662-distinct-prime-factor-count.apl
# apl-source:6

# apl-source:7
# كل عامل يعد مرة واحدة
# apl-source:8
# ننزع العامل بالكامل بعد عده
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
def عدد_العوامل(ن):
  # apl-source:19
  عد = 0
  # apl-source:20
  ك = 2
  # apl-source:21
  while ك * ك <= ن:
    # apl-source:22
    if ن % ك == 0:
      # apl-source:23
      عد = عد + 1
      # apl-source:24
      while ن % ك == 0:
        # apl-source:25
        ن = ن // ك
    # apl-source:26
    ك = ك + 1
  # apl-source:27
  if ن > 1:
    # apl-source:28
    عد = عد + 1
  # apl-source:29
  return عد
# apl-source:30

# apl-source:31
تأكد_يساوي(عدد_العوامل(12), 2, "اثنا عشر")
# apl-source:32
تأكد_يساوي(عدد_العوامل(30), 3, "ثلاثون")
# apl-source:33
تأكد_يساوي(عدد_العوامل(97), 1, "أولي")
# apl-source:34
تأكد_يساوي(عدد_العوامل(1), 0, "واحد")
# apl-source:35
