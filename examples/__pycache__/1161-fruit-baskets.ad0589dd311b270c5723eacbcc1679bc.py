
# apl-source:1
# مثال 1161 — سلال الفاكهة
# apl-source:2
# Fruit into baskets
# apl-source:3
# Demonstrates: نافذة منزلقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1161-fruit-baskets.apl
# apl-source:6

# apl-source:7
# مثل مسألة k حروف مختلفة مع k يساوي اثنين
# apl-source:8
# نعد الأنواع داخل النافذة
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
def اقصى_فاكهة(اشجار):
  # apl-source:19
  سلة = {}
  # apl-source:20
  يسار = 0
  # apl-source:21
  اقصى = 0
  # apl-source:22
  for يمين in range(len(اشجار)):
    # apl-source:23
    ن = اشجار[يمين]
    # apl-source:24
    سلة[ن] = سلة.get(ن, 0) + 1
    # apl-source:25
    while len(سلة) > 2:
      # apl-source:26
      سلة[اشجار[يسار]] = سلة[اشجار[يسار]] - 1
      # apl-source:27
      if سلة[اشجار[يسار]] == 0:
        # apl-source:28
        سلة.pop(اشجار[يسار])
      # apl-source:29
      يسار = يسار + 1
    # apl-source:30
    if يمين - يسار + 1 > اقصى:
      # apl-source:31
      اقصى = يمين - يسار + 1
  # apl-source:32
  return اقصى
# apl-source:33

# apl-source:34
تأكد_يساوي(اقصى_فاكهة([1,2,1]), 3, "ثلاث")
# apl-source:35
تأكد_يساوي(اقصى_فاكهة([0,1,2,2]), 3, "ثلاث ثانية")
# apl-source:36
تأكد_يساوي(اقصى_فاكهة([1,2,3,2,2]), 4, "أربع")
# apl-source:37
تأكد_يساوي(اقصى_فاكهة([3,3,3,1,2,1,1,2,3,3,4]), 5, "خمس")
# apl-source:38
