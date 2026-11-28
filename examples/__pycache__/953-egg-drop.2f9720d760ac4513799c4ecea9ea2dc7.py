
# apl-source:1
# مثال 953 — لغز إسقاط البيض
# apl-source:2
# Egg drop puzzle
# apl-source:3
# Demonstrates: أدنى أسوأ حالة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/953-egg-drop.apl
# apl-source:6

# apl-source:7
# لغز إسقاط البيض: أقل عدد محاولات مضمون بـ ك بيضة و ن طابقاً
# apl-source:8
# برمجة ديناميكية: ع[ب][ط] = 1 + أدنى(أعظم(كسر، نجاة))
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
def إسقاط(بيض, طوابق):
  # apl-source:19
  # ع السطر السابق والحالي
  # apl-source:20
  سابق = []
  # apl-source:21
  for _ in range(طوابق + 1):
    # apl-source:22
    سابق = سابق + [0]
  # apl-source:23
  for ب in range(1, بيض + 1):
    # apl-source:24
    حالي = []
    # apl-source:25
    حالي = حالي + [0]
    # apl-source:26
    for طابق in range(1, طوابق + 1):
      # apl-source:27
      if ب == 1:
        # apl-source:28
        حالي = حالي + [طابق]
      # apl-source:29
      else:
        # apl-source:30
        أدنى = طابق
        # apl-source:31
        for س in range(1, طابق + 1):
          # apl-source:32
          كسر = حالي[س - 1]
          # apl-source:33
          نجاة = سابق[طابق - س]
          # apl-source:34
          أسوأ = كسر
          # apl-source:35
          if نجاة > أسوأ:
            # apl-source:36
            أسوأ = نجاة
          # apl-source:37
          if 1 + أسوأ < أدنى:
            # apl-source:38
            أدنى = 1 + أسوأ
        # apl-source:39
        حالي = حالي + [أدنى]
    # apl-source:40
    سابق = حالي
  # apl-source:41
  return سابق[طوابق]
# apl-source:42

# apl-source:43
print("بيضتان 36 طابقاً:", إسقاط(2, 36))
# apl-source:44
print("بيضتان 100 طابق:", إسقاط(2, 100))
# apl-source:45
print("ثلاث بيضات 100 طابق:", إسقاط(3, 100))
# apl-source:46

# apl-source:47
تأكد_يساوي(إسقاط(2, 36), 8, "المثال الشهير 36")
# apl-source:48
تأكد_يساوي(إسقاط(2, 100), 14, "المثال الشهير 100")
# apl-source:49
تأكد_يساوي(إسقاط(3, 100), 9, "ثلاث بيضات أسرع")
# apl-source:50
تأكد_يساوي(إسقاط(1, 10), 10, "بيضة واحدة: خطي")
# apl-source:51
تأكد_يساوي(إسقاط(5, 1), 1, "طابق واحد")
# apl-source:52
