
# apl-source:1
# مثال 1469 — موعد الحافلة التالية
# apl-source:2
# Next bus arrival time
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1469-next-bus-arrival.apl
# apl-source:6

# apl-source:7
# الحافلات تمشي كل فترة ثابتة
# apl-source:8
# نقرب لأعلى لأقرب مضاعف
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
def الحافلة_التالية(بداية, فترة, وصول):
  # apl-source:19
  if وصول <= بداية:
    # apl-source:20
    return بداية
  # apl-source:21
  خطوات = (وصول - بداية + فترة - 1) // فترة
  # apl-source:22
  return بداية + خطوات * فترة
# apl-source:23

# apl-source:24
تأكد_يساوي(الحافلة_التالية(480, 15, 485), 495, "بعد قليل")
# apl-source:25
تأكد_يساوي(الحافلة_التالية(480, 15, 495), 495, "تماماً")
# apl-source:26
تأكد_يساوي(الحافلة_التالية(480, 15, 400), 480, "قبل البداية")
# apl-source:27
تأكد_يساوي(الحافلة_التالية(480, 20, 481), 500, "بعد الأولى")
# apl-source:28
