
# apl-source:1
# مثال 606 — مينيماكس بتقليم ألفا-بيتا
# apl-source:2
# Minimax alpha-beta
# apl-source:3
# Demonstrates: مينيماكس، تقليم، إكس-أو
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/606-minimax-ab.apl
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
# مينيماكس مع تقليم ألفا-بيتا: لعب مثالي في إكس-أو
# apl-source:25
# Demonstrates: بحث شجرة اللعبة, تقليم, تقييم المواقف
# apl-source:26
# X يلعب ليفوز و O ليمنعه؛ القيمة من منظور X
# apl-source:27

# apl-source:28
def فائز(لوحة):
  # apl-source:29
  خطوط = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  # apl-source:30
  for خط in خطوط:
    # apl-source:31
    أ = لوحة[خط[0]]
    # apl-source:32
    if أ != "" and أ == لوحة[خط[1]] and أ == لوحة[خط[2]]:
      # apl-source:33
      return أ
  # apl-source:34
  if "" in لوحة:
    # apl-source:35
    return ""
  # apl-source:36
  return "تعادل"
# apl-source:37

# apl-source:38
def مينيماكس(لوحة, دور_إكس, ألفا, بيتا):
  # apl-source:39
  نتيجة = فائز(لوحة)
  # apl-source:40
  if نتيجة == "X":
    # apl-source:41
    return 1
  # apl-source:42
  if نتيجة == "O":
    # apl-source:43
    return -1
  # apl-source:44
  if نتيجة == "تعادل":
    # apl-source:45
    return 0
  # apl-source:46
  if دور_إكس:
    # apl-source:47
    أفضل = -2
    # apl-source:48
    for ي in range(9):
      # apl-source:49
      if لوحة[ي] == "":
        # apl-source:50
        لوحة[ي] = "X"
        # apl-source:51
        أفضل = max(أفضل, مينيماكس(لوحة, False, ألفا, بيتا))
        # apl-source:52
        لوحة[ي] = ""
        # apl-source:53
        ألفا = max(ألفا, أفضل)
        # apl-source:54
        if بيتا <= ألفا:
          # apl-source:55
          return أفضل
    # apl-source:56
    return أفضل
  # apl-source:57
  أفضل = 2
  # apl-source:58
  for ي in range(9):
    # apl-source:59
    if لوحة[ي] == "":
      # apl-source:60
      لوحة[ي] = "O"
      # apl-source:61
      أفضل = min(أفضل, مينيماكس(لوحة, True, ألفا, بيتا))
      # apl-source:62
      لوحة[ي] = ""
      # apl-source:63
      بيتا = min(بيتا, أفضل)
      # apl-source:64
      if بيتا <= ألفا:
        # apl-source:65
        return أفضل
  # apl-source:66
  return أفضل
# apl-source:67

# apl-source:68
لوحة1 = ["X","X","","","","O","","O","",""]
# apl-source:69
تأكد_يساوي(مينيماكس(لوحة1, True, -2, 2), 1, "X يكمل الصف ويفوز")
# apl-source:70
لوحة2 = ["X","O","X","X","O","O","O","X",""]
# apl-source:71
تأكد_يساوي(مينيماكس(لوحة2, True, -2, 2), 0, "ملء الأخير تعادل")
# apl-source:72
لوحة3 = ["O","O","","X","X","","","",""]
# apl-source:73
تأكد_يساوي(مينيماكس(لوحة3, False, -2, 2), -1, "O يكمل الصف ويفوز")
# apl-source:74
print("تقييم الموقف الأول:", مينيماكس(لوحة1, True, -2, 2))
# apl-source:75
