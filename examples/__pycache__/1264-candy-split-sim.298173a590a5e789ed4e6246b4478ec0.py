
# apl-source:1
# مثال 1264 — تقسيم الحلوى
# apl-source:2
# Distribute candies to people
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1264-candy-split-sim.apl
# apl-source:6

# apl-source:7
# نعطي كل شخص ما يساوي رقم الدور
# apl-source:8
# وآخر دفعة تأخذ ما تبقى
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
def وزع(حلوى, اشخاص):
  # apl-source:19
  ناتج = [0] * اشخاص
  # apl-source:20
  ع = 0
  # apl-source:21
  while حلوى > 0:
    # apl-source:22
    ح = min(ع + 1, حلوى)
    # apl-source:23
    ناتج[ع % اشخاص] = ناتج[ع % اشخاص] + ح
    # apl-source:24
    حلوى = حلوى - ح
    # apl-source:25
    ع = ع + 1
  # apl-source:26
  return ناتج
# apl-source:27

# apl-source:28
تأكد_يساوي(وزع(7, 4), [1, 2, 3, 1], "سبع")
# apl-source:29
تأكد_يساوي(وزع(10, 3), [5, 2, 3], "عشر")
# apl-source:30
تأكد_يساوي(وزع(0, 3), [0, 0, 0], "لا حلوى")
# apl-source:31
