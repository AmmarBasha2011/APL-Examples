
# apl-source:1
# مثال 1247 — أصفار وآحاد
# apl-source:2
# Ones and zeroes subset
# apl-source:3
# Demonstrates: حقيبة ثنائية البعد
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1247-ones-and-zeroes.apl
# apl-source:6

# apl-source:7
# جدول لعدد الأصفار والآحاد المتاحة
# apl-source:8
# نحدثه عكسياً لكل نص
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
def اكبر_مجموعة(نصوص, م, ن):
  # apl-source:19
  د = []
  # apl-source:20
  for ع in range(م + 1):
    # apl-source:21
    د = د + [[0] * (ن + 1)]
  # apl-source:22
  for س in نصوص:
    # apl-source:23
    اصفار = 0
    # apl-source:24
    احاد = 0
    # apl-source:25
    for ح in س:
      # apl-source:26
      if ح == "0":
        # apl-source:27
        اصفار = اصفار + 1
      # apl-source:28
      else:
        # apl-source:29
        احاد = احاد + 1
    # apl-source:30
    for ا in range(م, اصفار - 1, -1):
      # apl-source:31
      for ب in range(ن, احاد - 1, -1):
        # apl-source:32
        if د[ا - اصفار][ب - احاد] + 1 > د[ا][ب]:
          # apl-source:33
          د[ا][ب] = د[ا - اصفار][ب - احاد] + 1
  # apl-source:34
  return د[م][ن]
# apl-source:35

# apl-source:36
تأكد_يساوي(اكبر_مجموعة(["10","0001","111001","1","0"], 5, 3), 4, "مثال أول")
# apl-source:37
تأكد_يساوي(اكبر_مجموعة(["10","0","1"], 1, 1), 2, "مثال ثان")
# apl-source:38
تأكد_يساوي(اكبر_مجموعة([], 3, 3), 0, "فارغة")
# apl-source:39
