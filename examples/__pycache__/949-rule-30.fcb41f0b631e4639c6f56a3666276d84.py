
# apl-source:1
# مثال 949 — الأتمتة الخلوية 30
# apl-source:2
# Rule 30 cellular automaton
# apl-source:3
# Demonstrates: يسار XOR وسط OR يمين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/949-rule-30.apl
# apl-source:6

# apl-source:7
# الأتمتة الخلوية قاعدة 30: فوضى من قاعدة محلية بسيطة
# apl-source:8
# الخلية الجديدة = يسار XOR (وسط OR يمين)
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
def خطوة(صف):
  # apl-source:19
  جديد = []
  # apl-source:20
  for i in range(len(صف)):
    # apl-source:21
    يسار = 0
    # apl-source:22
    if i > 0:
      # apl-source:23
      يسار = صف[i - 1]
    # apl-source:24
    يمين = 0
    # apl-source:25
    if i < len(صف) - 1:
      # apl-source:26
      يمين = صف[i + 1]
    # apl-source:27
    جديد = جديد + [يسار ^ (صف[i] | يمين)]
  # apl-source:28
  return جديد
# apl-source:29

# apl-source:30
def ارسم(صف):
  # apl-source:31
  نص = ""
  # apl-source:32
  for خلية in صف:
    # apl-source:33
    if خلية == 1:
      # apl-source:34
      نص = نص + "#"
    # apl-source:35
    else:
      # apl-source:36
      نص = نص + "."
  # apl-source:37
  return نص
# apl-source:38

# apl-source:39
صف = [0, 0, 0, 1, 0, 0, 0]
# apl-source:40
خطوة1 = خطوة(صف)
# apl-source:41
خطوة2 = خطوة(خطوة1)
# apl-source:42
خطوة3 = خطوة(خطوة2)
# apl-source:43
print("1:", ارسم(خطوة1))
# apl-source:44
print("2:", ارسم(خطوة2))
# apl-source:45
print("3:", ارسم(خطوة3))
# apl-source:46

# apl-source:47
تأكد_يساوي(ارسم(خطوة1), "..###..", "الخطوة الأولى")
# apl-source:48
تأكد_يساوي(ارسم(خطوة2), ".##..#.", "الخطوة الثانية")
# apl-source:49
تأكد_يساوي(ارسم(خطوة3), "##.####", "الخطوة الثالثة")
# apl-source:50

# apl-source:51
# حتمية: إعادة الحساب تعطي نفس النتيجة
# apl-source:52
تأكد_يساوي(ارسم(خطوة(خطوة(صف))), ارسم(خطوة2), "حتمية")
# apl-source:53

# apl-source:54
# من بذرة واحدة بعد 10 خطوات يمتلئ أكثر من نصف العرض الأيسر
# apl-source:55
عريض = [0]
# apl-source:56
for _ in range(40):
  # apl-source:57
  عريض = عريض + [0]
# apl-source:58
عريض[20] = 1
# apl-source:59
جاري = عريض
# apl-source:60
for _ in range(10):
  # apl-source:61
  جاري = خطوة(جاري)
# apl-source:62
عدد = 0
# apl-source:63
for خلية in جاري:
  # apl-source:64
  عدد = عدد + خلية
# apl-source:65
if عدد < 10:
  # apl-source:66
  print("فشل: النمو ضعيف", عدد)
  # apl-source:67
  قياسي_نظام_اخرج(1)
# apl-source:68
print("ناجح: نمو القاعدة 30 =", عدد, "خلية حية")
# apl-source:69
