
# apl-source:1
# مثال 1950 — أطول سلسلة أيام دافئة
# apl-source:2
# Longest warm streak
# apl-source:3
# Demonstrates: نوافذ
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1950-longest-warm-streak-days.apl
# apl-source:6

# apl-source:7
# # نزيد العداد عند يوم دافئ ونصفره عند غيره
# apl-source:8
# # ونحتفظ بأكبر قيمة
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
def اطول_سلسلة(حرارة, حد):
  # apl-source:19
  حالي = 0
  # apl-source:20
  افضل = 0
  # apl-source:21
  for ح in حرارة:
    # apl-source:22
    if ح > حد:
      # apl-source:23
      حالي = حالي + 1
      # apl-source:24
      افضل = max(افضل, حالي)
    # apl-source:25
    else:
      # apl-source:26
      حالي = 0
  # apl-source:27
  return افضل
# apl-source:28

# apl-source:29
تأكد_يساوي(اطول_سلسلة([30, 31, 25, 32, 33, 34, 20], 29), 3, "ثلاثة")
# apl-source:30
تأكد_يساوي(اطول_سلسلة([10, 12], 20), 0, "لا يوجد")
# apl-source:31
تأكد_يساوي(اطول_سلسلة([], 5), 0, "فارغ")
# apl-source:32
