
# apl-source:1
# مثال 1769 — الزاوية بين عقربي الساعة
# apl-source:2
# Angle between clock hands
# apl-source:3
# Demonstrates: وقت
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1769-clock-angle-between-hands.apl
# apl-source:6

# apl-source:7
# عقرب الدقائق 6 درجات للدقيقة
# apl-source:8
# عقرب الساعات نصف درجة للدقيقة
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
def زاوية(ساعة, دقيقة):
  # apl-source:19
  د2 = دقيقة * 12
  # apl-source:20
  س2 = (ساعة % 12) * 60 + دقيقة
  # apl-source:21
  فرق = س2 - د2
  # apl-source:22
  if فرق < 0:
    # apl-source:23
    فرق = -فرق
  # apl-source:24
  if فرق > 360:
    # apl-source:25
    فرق = 720 - فرق
  # apl-source:26
  return فرق / 2
# apl-source:27

# apl-source:28
تأكد_يساوي(زاوية(3, 0), 90, "ثلاثة")
# apl-source:29
تأكد_يساوي(زاوية(12, 0), 0, "اثنا عشر")
# apl-source:30
تأكد_يساوي(زاوية(6, 0), 180, "ستة")
# apl-source:31
تأكد_يساوي(زاوية(9, 0), 90, "تسعة")
# apl-source:32
