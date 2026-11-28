
# apl-source:1
# مثال 1272 — حجوزات رحلات
# apl-source:2
# Corporate flight bookings
# apl-source:3
# Demonstrates: فروق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1272-corporate-flight-bookings.apl
# apl-source:6

# apl-source:7
# كل حجز مجال رحلات بعدد مقاعد
# apl-source:8
# نستخدم مصفوفة الفروق
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
def حجوزات(حجوز, ن):
  # apl-source:19
  فروق = [0] * (ن + 1)
  # apl-source:20
  for ح in حجوز:
    # apl-source:21
    فروق[ح[0] - 1] = فروق[ح[0] - 1] + ح[2]
    # apl-source:22
    فروق[ح[1]] = فروق[ح[1]] - ح[2]
  # apl-source:23
  ناتج = []
  # apl-source:24
  مج = 0
  # apl-source:25
  for ع in range(ن):
    # apl-source:26
    مج = مج + فروق[ع]
    # apl-source:27
    ناتج = ناتج + [مج]
  # apl-source:28
  return ناتج
# apl-source:29

# apl-source:30
تأكد_يساوي(حجوزات([[1,2,10],[2,3,20],[2,5,25]], 5), [10,55,45,25,25], "مثال أول")
# apl-source:31
تأكد_يساوي(حجوزات([[1,2,10],[2,2,15]], 2), [10,25], "مثال ثان")
# apl-source:32
