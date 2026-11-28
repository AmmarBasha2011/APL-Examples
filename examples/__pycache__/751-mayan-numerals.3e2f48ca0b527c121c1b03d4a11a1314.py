
# apl-source:1
# مثال 751 — أرقام المايا
# apl-source:2
# Mayan numerals
# apl-source:3
# Demonstrates: أساس 20، نقاط وأصابع، صفر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/751-mayan-numerals.apl
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
# أرقام المايا: نظام عشريني بنقاط وأصابع
# apl-source:25
# Demonstrates: أساس 20, خانة = أصابع ▬ (خمسات) ونقاط •, صفر صدفي
# apl-source:26
# كل خانة 0..19: أصبع لكل خمسة ونقطة لكل واحد
# apl-source:27

# apl-source:28
def ارسم_خانة(خانة):
  # apl-source:29
  if خانة == 0:
    # apl-source:30
    return "0"
  # apl-source:31
  ناتج = ""
  # apl-source:32
  for ي in range(خانة // 5):
    # apl-source:33
    ناتج = ناتج + "▬"
  # apl-source:34
  for ي in range(خانة % 5):
    # apl-source:35
    ناتج = ناتج + "•"
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
def إلى_مايا(عدد):
  # apl-source:39
  if عدد == 0:
    # apl-source:40
    return ["0"]
  # apl-source:41
  خانات = []
  # apl-source:42
  باقي = عدد
  # apl-source:43
  while باقي > 0:
    # apl-source:44
    خانات = [باقي % 20] + خانات
    # apl-source:45
    باقي = باقي // 20
  # apl-source:46
  ناتج = []
  # apl-source:47
  for خ in خانات:
    # apl-source:48
    ناتج.append(ارسم_خانة(خ))
  # apl-source:49
  return ناتج
# apl-source:50

# apl-source:51
def من_مايا(خانات_رقمية):
  # apl-source:52
  قيمة = 0
  # apl-source:53
  for خ in خانات_رقمية:
    # apl-source:54
    قيمة = قيمة * 20 + خ
  # apl-source:55
  return قيمة
# apl-source:56

# apl-source:57
تأكد_يساوي(ارسم_خانة(0), "0", "الصفر الصدفي")
# apl-source:58
تأكد_يساوي(ارسم_خانة(5), "▬", "خمسة أصبع")
# apl-source:59
تأكد_يساوي(ارسم_خانة(13), "▬▬•••", "ثلاثة عشر")
# apl-source:60
تأكد_يساوي(ارسم_خانة(19), "▬▬▬••••", "تسعة عشر")
# apl-source:61

# apl-source:62
تأكد_يساوي(إلى_مايا(20), ["•", "0"], "عشرون = نقطة فوق صفر")
# apl-source:63
تأكد_يساوي(إلى_مايا(42), ["••", "••"], "اثنان وأربعون")
# apl-source:64
تأكد_يساوي(إلى_مايا(365), ["▬▬▬•••", "▬"], "أيام السنة")
# apl-source:65
تأكد_يساوي(إلى_مايا(400), ["•", "0", "0"], "مربع عشرين")
# apl-source:66

# apl-source:67
تأكد_يساوي(من_مايا([2, 2]), 42, "قراءة عكسية")
# apl-source:68
تأكد_يساوي(من_مايا([18, 5]), 365, "قراءة عكسية للسنة")
# apl-source:69

# apl-source:70
print("365 =", إلى_مايا(365))
# apl-source:71
