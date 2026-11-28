
# apl-source:1
# مثال 1552 — حجم المنشور الثلاثي
# apl-source:2
# Triangular prism volume
# apl-source:3
# Demonstrates: هندسة ثلاثية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1552-triangular-prism-volume.apl
# apl-source:6

# apl-source:7
# مساحة المثلث نصف القاعدة في الارتفاع
# apl-source:8
# نضربها في الطول
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
def حجم_المنشور(قاعدة, ارتفاع, طول_):
  # apl-source:19
  return قاعدة * ارتفاع / 2 * طول_
# apl-source:20

# apl-source:21
تأكد_يساوي(حجم_المنشور(4, 3, 10), 60.0, "أربعة وثلاثة")
# apl-source:22
تأكد_يساوي(حجم_المنشور(2, 2, 2), 4.0, "صغير")
# apl-source:23
تأكد_يساوي(حجم_المنشور(5, 0, 7), 0.0, "مسطح")
# apl-source:24
