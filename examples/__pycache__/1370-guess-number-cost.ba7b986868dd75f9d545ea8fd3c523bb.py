
# apl-source:1
# مثال 1370 — كلفة التخمين
# apl-source:2
# Guess number higher or lower cost
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1370-guess-number-cost.apl
# apl-source:6

# apl-source:7
# كل تخمين خاطئ يكلف قيمة الرقم
# apl-source:8
# نختار التخمين الذي يقلل أسوأ حالة
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
def كلفة_ضمان(ن):
  # apl-source:19
  د = []
  # apl-source:20
  for ع in range(ن + 2):
    # apl-source:21
    د = د + [[0] * (ن + 2)]
  # apl-source:22
  for طول_ in range(2, ن + 1):
    # apl-source:23
    for بداية in range(1, ن - طول_ + 2):
      # apl-source:24
      نهاية = بداية + طول_ - 1
      # apl-source:25
      افضل = 1000000000
      # apl-source:26
      for ك in range(بداية, نهاية + 1):
        # apl-source:27
        كلفة = ك + max(د[بداية][ك - 1], د[ك + 1][نهاية])
        # apl-source:28
        if كلفة < افضل:
          # apl-source:29
          افضل = كلفة
      # apl-source:30
      د[بداية][نهاية] = افضل
  # apl-source:31
  return د[1][ن]
# apl-source:32

# apl-source:33
تأكد_يساوي(كلفة_ضمان(10), 16, "عشرة")
# apl-source:34
تأكد_يساوي(كلفة_ضمان(1), 0, "واحد")
# apl-source:35
تأكد_يساوي(كلفة_ضمان(2), 1, "اثنان")
# apl-source:36
