
# apl-source:1
# مثال 961 — قطر الشجرة
# apl-source:2
# Tree diameter
# apl-source:3
# Demonstrates: مسحان عرضيان متتاليان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/961-tree-diameter.apl
# apl-source:6

# apl-source:7
# قطر الشجرة: أطول مسار بين عقدتين عبر مسحين عرضيين
# apl-source:8
# أول مسح يجد طرفاً بعيداً، وثاني مسح منه يعطي القطر
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
جوار = [[], [], [], [], []]
# apl-source:19
حواف = [[0, 1], [1, 2], [2, 3], [1, 4]]
# apl-source:20
for ح in حواف:
  # apl-source:21
  جوار[ح[0]] = جوار[ح[0]] + [ح[1]]
  # apl-source:22
  جوار[ح[1]] = جوار[ح[1]] + [ح[0]]
# apl-source:23

# apl-source:24
def أبعد(بداية):
  # apl-source:25
  مسافات = [-1, -1, -1, -1, -1]
  # apl-source:26
  مسافات[بداية] = 0
  # apl-source:27
  طابور = [بداية]
  # apl-source:28
  رأس = 0
  # apl-source:29
  while رأس < len(طابور):
    # apl-source:30
    عقدة = طابور[رأس]
    # apl-source:31
    رأس = رأس + 1
    # apl-source:32
    for جار in جوار[عقدة]:
      # apl-source:33
      if مسافات[جار] == -1:
        # apl-source:34
        مسافات[جار] = مسافات[عقدة] + 1
        # apl-source:35
        طابور = طابور + [جار]
  # apl-source:36
  أفضل = 0
  # apl-source:37
  أقصى = -1
  # apl-source:38
  for عقدة2 in range(5):
    # apl-source:39
    if مسافات[عقدة2] > أقصى:
      # apl-source:40
      أقصى = مسافات[عقدة2]
      # apl-source:41
      أفضل = عقدة2
  # apl-source:42
  return [أفضل, أقصى]
# apl-source:43

# apl-source:44
أول = أبعد(0)
# apl-source:45
ثان = أبعد(أول[0])
# apl-source:46
تأكد_يساوي(أول[0], 3, "أبعد عقدة عن الصفر")
# apl-source:47
تأكد_يساوي(ثان[1], 3, "قطر الشجرة")
# apl-source:48
