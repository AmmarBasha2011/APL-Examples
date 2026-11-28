
# apl-source:1
# مثال 609 — لعبة الحرب بالورق
# apl-source:2
# Card war simulation
# apl-source:3
# Demonstrates: ورق، محاكاة، جولات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/609-card-war.apl
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
# لعبة الحرب بالورق: محاكاة كاملة بمجموعتين ثابتتين
# apl-source:25
# Demonstrates: طابوران, جولات حرب بالتعادل, ثوابت اللعبة
# apl-source:26
# القاعدة: الأعلى يأخذ الورقتين، وعند التعادل حرب بثلاث ورقات
# apl-source:27

# apl-source:28
def العب_الحرب(يد_أ, يد_ب):
  # apl-source:29
  جولات = 0
  # apl-source:30
  while len(يد_أ) > 0 and len(يد_ب) > 0 and جولات < 5000:
    # apl-source:31
    جولات = جولات + 1
    # apl-source:32
    غنيمة = []
    # apl-source:33
    أ = يد_أ.pop(0)
    # apl-source:34
    ب = يد_ب.pop(0)
    # apl-source:35
    غنيمة.append(أ)
    # apl-source:36
    غنيمة.append(ب)
    # apl-source:37
    while أ == ب and len(يد_أ) >= 2 and len(يد_ب) >= 2:
      # apl-source:38
      for ك in range(2):
        # apl-source:39
        غنيمة.append(يد_أ.pop(0))
        # apl-source:40
        غنيمة.append(يد_ب.pop(0))
      # apl-source:41
      أ = يد_أ.pop(0)
      # apl-source:42
      ب = يد_ب.pop(0)
      # apl-source:43
      غنيمة.append(أ)
      # apl-source:44
      غنيمة.append(ب)
    # apl-source:45
    if أ > ب:
      # apl-source:46
      for ورقة in غنيمة:
        # apl-source:47
        يد_أ.append(ورقة)
    # apl-source:48
    else:
      # apl-source:49
      for ورقة in غنيمة:
        # apl-source:50
        يد_ب.append(ورقة)
  # apl-source:51
  return [len(يد_أ), len(يد_ب), جولات]
# apl-source:52

# apl-source:53
يد_أ = [2, 5, 8, 11, 3, 6]
# apl-source:54
يد_ب = [4, 7, 10, 12, 9, 1]
# apl-source:55
نتيجة = العب_الحرب(يد_أ, يد_ب)
# apl-source:56
print("النهاية: أ =", نتيجة[0], " ب =", نتيجة[1], " جولات =", نتيجة[2])
# apl-source:57
تأكد_يساوي(نتيجة[0] + نتيجة[1], 12, "الأوراق محفوظة")
# apl-source:58
تأكد_يساوي(نتيجة[0] == 0 or نتيجة[1] == 0, True, "فائز حاسم")
# apl-source:59
تأكد_يساوي(نتيجة[2] > 0, True, "جولة واحدة على الأقل")
# apl-source:60
