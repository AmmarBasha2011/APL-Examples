
# apl-source:1
# مثال 1706 — أقل قفزات للنهاية
# apl-source:2
# Minimum jumps to reach the end
# apl-source:3
# Demonstrates: جشع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1706-min-jumps-to-end.apl
# apl-source:6

# apl-source:7
# نتتبع نهاية القفزة الحالية
# apl-source:8
# نزيد القفزات عند بلوغها
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
def أقل_قفزات(ق):
  # apl-source:19
  if len(ق) <= 1:
    # apl-source:20
    return 0
  # apl-source:21
  قفزات = 0
  # apl-source:22
  نهاية = 0
  # apl-source:23
  أبعد = 0
  # apl-source:24
  for ك in range(len(ق) - 1):
    # apl-source:25
    أبعد = max(أبعد, ك + ق[ك])
    # apl-source:26
    if ك == نهاية:
      # apl-source:27
      قفزات = قفزات + 1
      # apl-source:28
      نهاية = أبعد
  # apl-source:29
  return قفزات
# apl-source:30

# apl-source:31
تأكد_يساوي(أقل_قفزات([2, 3, 1, 1, 4]), 2, "اثنان")
# apl-source:32
تأكد_يساوي(أقل_قفزات([1, 1, 1, 1]), 3, "ثلاثة")
# apl-source:33
تأكد_يساوي(أقل_قفزات([5]), 0, "واحد")
# apl-source:34
