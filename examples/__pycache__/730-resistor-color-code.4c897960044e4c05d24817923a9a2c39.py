
# apl-source:1
# مثال 730 — ألوان المقاومات
# apl-source:2
# Resistor color code
# apl-source:3
# Demonstrates: أشرطة، مضاعف، فك وشفر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/730-resistor-color-code.apl
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
# شفرة ألوان المقاومات
# apl-source:25
# Demonstrates: ألوان كأرقام, مضاعف عشري, تنسيق kΩ و MΩ
# apl-source:26
# أسود بني أحمر برتقالي أصفر أخضر أزرق بنفسجي رمادي أبيض = 0..9
# apl-source:27

# apl-source:28
ألوان = ["أسود", "بني", "أحمر", "برتقالي", "أصفر", "أخضر", "أزرق", "بنفسجي", "رمادي", "أبيض"]
# apl-source:29

# apl-source:30
def رقم_لون(لون):
  # apl-source:31
  for ي in range(10):
    # apl-source:32
    if ألوان[ي] == لون:
      # apl-source:33
      return ي
  # apl-source:34
  return -1
# apl-source:35

# apl-source:36
قوى_عشرة = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
# apl-source:37

# apl-source:38
def فك(أول, ثان, مضاعف):
  # apl-source:39
  قيمة = (رقم_لون(أول) * 10 + رقم_لون(ثان)) * قوى_عشرة[رقم_لون(مضاعف)]
  # apl-source:40
  return قيمة
# apl-source:41

# apl-source:42
def صغ(قيمة):
  # apl-source:43
  if قيمة >= 1000000:
    # apl-source:44
    return str(قيمة // 1000000) + "MΩ"
  # apl-source:45
  if قيمة >= 1000:
    # apl-source:46
    return str(قيمة // 1000) + "kΩ"
  # apl-source:47
  return str(قيمة) + "Ω"
# apl-source:48

# apl-source:49
def شفر(قيمة):
  # apl-source:50
  مضاعف = 0
  # apl-source:51
  أساس = قيمة
  # apl-source:52
  while أساس >= 100:
    # apl-source:53
    أساس = أساس // 10
    # apl-source:54
    مضاعف = مضاعف + 1
  # apl-source:55
  أول = أساس // 10
  # apl-source:56
  ثان = أساس % 10
  # apl-source:57
  return [ألوان[أول], ألوان[ثان], ألوان[مضاعف]]
# apl-source:58

# apl-source:59
تأكد_يساوي(رقم_لون("أحمر"), 2, "أحمر اثنان")
# apl-source:60
تأكد_يساوي(فك("بني", "أسود", "أحمر"), 1000, "بني أسود أحمر ألف")
# apl-source:61
تأكد_يساوي(فك("أصفر", "بنفسجي", "أحمر"), 4700, "4700 أوم")
# apl-source:62
تأكد_يساوي(صغ(فك("أصفر", "بنفسجي", "أحمر")), "4kΩ", "تنسيق كيلو")
# apl-source:63
تأكد_يساوي(صغ(220), "220Ω", "تنسيق أوم")
# apl-source:64
تأكد_يساوي(صغ(فك("بني", "أسود", "أخضر")), "1MΩ", "تنسيق ميغا")
# apl-source:65
تأكد_يساوي(شفر(4700), ["أصفر", "بنفسجي", "أحمر"], "الشفر العكسي")
# apl-source:66
تأكد_يساوي(فك(شفر(5600)[0], شفر(5600)[1], شفر(5600)[2]), 5600, "ذهاب وعودة")
# apl-source:67
print("4700 =", شفر(4700))
# apl-source:68
