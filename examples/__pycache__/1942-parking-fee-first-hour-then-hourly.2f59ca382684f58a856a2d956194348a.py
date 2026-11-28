
# apl-source:1
# مثال 1942 — حساب رسوم موقف السيارات
# apl-source:2
# Parking lot fee calculator
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1942-parking-fee-first-hour-then-hourly.apl
# apl-source:6

# apl-source:7
# # نقرب الدقائق لأعلى إلى س_كلية كاملة
# apl-source:8
# # ونطبق السقف اليومي على المجموع
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
def الرسوم(دقائق_كلية):
  # apl-source:19
  س_كلية = (دقائق_كلية + 59) // 60
  # apl-source:20
  if س_كلية == 0:
    # apl-source:21
    return 0
  # apl-source:22
  مبلغ = 10 + (س_كلية - 1) * 6
  # apl-source:23
  return min(مبلغ, 60)
# apl-source:24

# apl-source:25
تأكد_يساوي(الرسوم(0), 0, "صفر")
# apl-source:26
تأكد_يساوي(الرسوم(45), 10, "أقل من ساعة")
# apl-source:27
تأكد_يساوي(الرسوم(61), 16, "ساعتان")
# apl-source:28
تأكد_يساوي(الرسوم(300), 34, "خمس س_كلية")
# apl-source:29
تأكد_يساوي(الرسوم(1440), 60, "السقف")
# apl-source:30
