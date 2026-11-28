
# apl-source:1
# مثال 879 — شجرة ستيرن-بروكو
# apl-source:2
# Stern-Brocot tree
# apl-source:3
# Demonstrates: وسط حسابي بين حدين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/879-stern-brocot.apl
# apl-source:6

# apl-source:7
# شجرة ستيرن-بروكو: مسار كل كسر موجب مختزل بين 0/1 و1/0
# apl-source:8
# المسار L/R يشكل تمثيلاً فريداً ويطابق الكسر المستمر
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
def مسار_ستيرن_بروكو(بسط, مقام):
  # apl-source:19
  أدنى_ب = 0
  # apl-source:20
  أدنى_م = 1
  # apl-source:21
  أعلى_ب = 1
  # apl-source:22
  أعلى_م = 0
  # apl-source:23
  مسار = ""
  # apl-source:24
  while 1 == 1:
    # apl-source:25
    وسط_ب = أدنى_ب + أعلى_ب
    # apl-source:26
    وسط_م = أدنى_م + أعلى_م
    # apl-source:27
    if (وسط_ب == بسط) and (وسط_م == مقام):
      # apl-source:28
      return مسار
    # apl-source:29
    if بسط * وسط_م < مقام * وسط_ب:
      # apl-source:30
      مسار = مسار + "L"
      # apl-source:31
      أعلى_ب = وسط_ب
      # apl-source:32
      أعلى_م = وسط_م
    # apl-source:33
    else:
      # apl-source:34
      مسار = مسار + "R"
      # apl-source:35
      أدنى_ب = وسط_ب
      # apl-source:36
      أدنى_م = وسط_م
# apl-source:37

# apl-source:38
مسار = مسار_ستيرن_بروكو(5, 7)
# apl-source:39
print("مسار 5/7:", مسار)
# apl-source:40

# apl-source:41
تأكد_يساوي(مسار, "LRRL", "مسار 5/7 هو LRRL")
# apl-source:42
تأكد_يساوي(مسار_ستيرن_بروكو(1, 2), "L", "1/2 خطوة يسار")
# apl-source:43
تأكد_يساوي(مسار_ستيرن_بروكو(2, 3), "LR", "2/3 = LR")
# apl-source:44
تأكد_يساوي(مسار_ستيرن_بروكو(3, 1), "RR", "3/1 = RR")
# apl-source:45

# apl-source:46
# إعادة البناء من المسار تعيد الكسر
# apl-source:47
def ابن_من_مسار(مسار):
  # apl-source:48
  أدنى_ب = 0
  # apl-source:49
  أدنى_م = 1
  # apl-source:50
  أعلى_ب = 1
  # apl-source:51
  أعلى_م = 0
  # apl-source:52
  for i in range(len(مسار)):
    # apl-source:53
    وسط_ب = أدنى_ب + أعلى_ب
    # apl-source:54
    وسط_م = أدنى_م + أعلى_م
    # apl-source:55
    if مسار[i] == "L":
      # apl-source:56
      أعلى_ب = وسط_ب
      # apl-source:57
      أعلى_م = وسط_م
    # apl-source:58
    else:
      # apl-source:59
      أدنى_ب = وسط_ب
      # apl-source:60
      أدنى_م = وسط_م
  # apl-source:61
  return [أدنى_ب + أعلى_ب, أدنى_م + أعلى_م]
# apl-source:62

# apl-source:63
كسر = ابن_من_مسار("LRRL")
# apl-source:64
تأكد_يساوي(كسر[0], 5, "إعادة البناء: البسط")
# apl-source:65
تأكد_يساوي(كسر[1], 7, "إعادة البناء: المقام")
# apl-source:66
