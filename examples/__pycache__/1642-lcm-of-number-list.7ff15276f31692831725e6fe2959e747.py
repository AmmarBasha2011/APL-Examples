
# apl-source:1
# مثال 1642 — المضاعف المشترك الأصغر لقائمة
# apl-source:2
# LCM of a list of numbers
# apl-source:3
# Demonstrates: نظرية الأعداد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1642-lcm-of-number-list.apl
# apl-source:6

# apl-source:7
# م.م.أ(أ,ب) = أ × ب ÷ القاسم
# apl-source:8
# نكرر على القائمة
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
def قاسم(أ, ب):
  # apl-source:19
  while ب != 0:
    # apl-source:20
    ت = ب
    # apl-source:21
    ب = أ % ب
    # apl-source:22
    أ = ت
  # apl-source:23
  return أ
# apl-source:24

# apl-source:25
def مضاعف_القائمة(ق):
  # apl-source:26
  ناتج = 1
  # apl-source:27
  for ع in ق:
    # apl-source:28
    ناتج = ناتج * ع // قاسم(ناتج, ع)
  # apl-source:29
  return ناتج
# apl-source:30

# apl-source:31
تأكد_يساوي(مضاعف_القائمة([4, 6]), 12, "اثنا عشر")
# apl-source:32
تأكد_يساوي(مضاعف_القائمة([1, 2, 3, 4, 5]), 60, "ستون")
# apl-source:33
تأكد_يساوي(مضاعف_القائمة([7]), 7, "واحد")
# apl-source:34
