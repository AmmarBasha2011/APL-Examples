
# apl-source:1
# مثال 789 — مولد LFSR
# apl-source:2
# LFSR PRNG
# apl-source:3
# Demonstrates: taps فيبوناتشي، باريتي، إزاحة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/789-lfsr-prng.apl
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
# مولد أعداد شبه عشوائية LFSR فيبوناتشي 16 بت
# apl-source:25
# Demonstrates: مسجل إزاحة بخطي راجع, حساب الباريتي, توليد بايتات عشوائية
# apl-source:26

# apl-source:27
def لفسر_خطوة(س):
  # apl-source:28
  # مص taps في مواضع 16,14,13,11 يساوي 0xD008
  # apl-source:29
  م = س & 53256
  # apl-source:30
  بت = 0
  # apl-source:31
  while م > 0:
    # apl-source:32
    بت = بت ^ (م & 1)
    # apl-source:33
    م = م // 2
  # apl-source:34
  return (س // 2) | (بت * 32768)
# apl-source:35

# apl-source:36
س = 44257
# apl-source:37
تأكد_يساوي(لفسر_خطوة(س), 54896, "الحالة الأولى")
# apl-source:38
س = لفسر_خطوة(س)
# apl-source:39
تأكد_يساوي(س, 54896, "تحقق الإسناد")
# apl-source:40
سلسلة = []
# apl-source:41
for ي in range(5):
  # apl-source:42
  س = لفسر_خطوة(س)
  # apl-source:43
  سلسلة.append(س)
# apl-source:44
تأكد_يساوي(سلسلة, [60216, 62876, 31438, 48487, 24243], "خمس حالات")
# apl-source:45
س = 44257
# apl-source:46
for ي in range(100):
  # apl-source:47
  س = لفسر_خطوة(س)
# apl-source:48
تأكد_يساوي(س, 64154, "الحالة المئة")
# apl-source:49
بايتات = []
# apl-source:50
for ي in range(4):
  # apl-source:51
  س = لفسر_خطوة(س)
  # apl-source:52
  بايتات.append(س & 255)
# apl-source:53
تأكد_يساوي(بايتات, [77, 166, 83, 169], "بايتات عشوائية")
# apl-source:54
