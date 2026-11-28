
# apl-source:1
# مثال 1176 — موعد مشترك
# apl-source:2
# Common meeting slot
# apl-source:3
# Demonstrates: مؤشران
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1176-meeting-scheduler-slot.apl
# apl-source:6

# apl-source:7
# نمشي على الجدولين المرتبين
# apl-source:8
# ونقارن تقاطع الفترتين بالمدة المطلوبة
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
def فترة_مشتركة(أ, ب, مدة):
  # apl-source:19
  ي = 0
  # apl-source:20
  ك = 0
  # apl-source:21
  while (ي < len(أ)) and (ك < len(ب)):
    # apl-source:22
    بداية = max(أ[ي][0], ب[ك][0])
    # apl-source:23
    نهاية = min(أ[ي][1], ب[ك][1])
    # apl-source:24
    if نهاية - بداية >= مدة:
      # apl-source:25
      return [بداية, بداية + مدة]
    # apl-source:26
    if أ[ي][1] < ب[ك][1]:
      # apl-source:27
      ي = ي + 1
    # apl-source:28
    else:
      # apl-source:29
      ك = ك + 1
  # apl-source:30
  return []
# apl-source:31

# apl-source:32
أ = [[10,50],[60,120],[140,210]]
# apl-source:33
ب = [[0,15],[60,70]]
# apl-source:34
تأكد_يساوي(فترة_مشتركة(أ, ب, 8), [60, 68], "ثماني دقائق")
# apl-source:35
تأكد_يساوي(فترة_مشتركة(أ, ب, 12), [], "لا فترة")
# apl-source:36
تأكد_يساوي(فترة_مشتركة([[0,10]], [[0,10]], 10), [0, 10], "كاملة")
# apl-source:37
