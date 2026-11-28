
# apl-source:1
# مثال 1462 — الزاوية بين عقربي الساعة
# apl-source:2
# Angle between clock hands
# apl-source:3
# Demonstrates: حسابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1462-clock-hands-angle.apl
# apl-source:6

# apl-source:7
# عقرب الساعات يتحرك نصف درجة كل دقيقة
# apl-source:8
# عقرب الدقائق ست درجات كل دقيقة
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
def زاوية_الساعة(ساعة, دقيقة):
  # apl-source:19
  ع_ساعة = (ساعة % 12) * 30 + دقيقة * 0.5
  # apl-source:20
  ع_دقيقة = دقيقة * 6
  # apl-source:21
  فرق = ع_ساعة - ع_دقيقة
  # apl-source:22
  if فرق < 0:
    # apl-source:23
    فرق = -فرق
  # apl-source:24
  if فرق > 180:
    # apl-source:25
    فرق = 360 - فرق
  # apl-source:26
  return فرق
# apl-source:27

# apl-source:28
تأكد_يساوي(زاوية_الساعة(3, 0), 90.0, "الثالثة")
# apl-source:29
تأكد_يساوي(زاوية_الساعة(12, 30), 165.0, "منتصف")
# apl-source:30
تأكد_يساوي(زاوية_الساعة(6, 0), 180.0, "السادسة")
# apl-source:31
تأكد_يساوي(زاوية_الساعة(9, 15), 172.5, "التاسعة والربع")
# apl-source:32
