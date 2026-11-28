
# apl-source:1
# مثال 643 — عداد التاكسي الأبيض
# apl-source:2
# Cairo taxi fare
# apl-source:3
# Demonstrates: عداد، تعريفة، القاهرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/643-cairo-taxi-fare.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# عداد التاكسي الأبيض في القاهرة (تعريفة تقريبية)
# apl-source:25
# Demonstrates: فتحة عداد, سعر كيلومتر, كسور, تقريب
# apl-source:26
# فتحة ثم سعر لكل كيلومتر إضافي
# apl-source:27

# apl-source:28
def أجرة(كيلومترات):
  # apl-source:29
  فتحة = 10
  # apl-source:30
  أول_كم = 8
  # apl-source:31
  إضافي = 5
  # apl-source:32
  if كيلومترات <= 1:
    # apl-source:33
    return فتحة + أول_كم
  # apl-source:34
  return فتحة + أول_كم + int((كيلومترات - 1) * إضافي + 0.5)
# apl-source:35

# apl-source:36
تأكد_يساوي(أجرة(1), 18, "كيلومتر واحد")
# apl-source:37
تأكد_يساوي(أجرة(3), 28, "ثلاثة كيلومترات")
# apl-source:38
تأكد_يساوي(أجرة(10), 63, "عشرة كيلومترات")
# apl-source:39
print("رحلة 7 كم:", أجرة(7), "جنيه")
# apl-source:40
تأكد_يساوي(أجرة(7), 48, "سبعة كيلومترات")
# apl-source:41
