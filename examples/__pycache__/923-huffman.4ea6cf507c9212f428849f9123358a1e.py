
# apl-source:1
# مثال 923 — ترميز هوفمان
# apl-source:2
# Huffman coding
# apl-source:3
# Demonstrates: دمج أقل عقدتين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/923-huffman.apl
# apl-source:6

# apl-source:7
# ترميز هوفمان: رموز بطول متغير حسب التكرار
# apl-source:8
# جشع: ادمج أقل عقدتين تكراراً حتى تبقى جذراً واحداً
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
# العقد: [تكرار, أحرف]، ونبني الشيفرات عند الدمج
# apl-source:19
def هوفمان(أحرف, تكرارات):
  # apl-source:20
  ن = len(أحرف)
  # apl-source:21
  عقد = []
  # apl-source:22
  for i in range(ن):
    # apl-source:23
    عقد = عقد + [[تكرارات[i], [أحرف[i]], ""]]
  # apl-source:24
  # شيفرات نهائية لكل حرف
  # apl-source:25
  شيفرات = []
  # apl-source:26
  for i in range(ن):
    # apl-source:27
    شيفرات = شيفرات + [""]
  # apl-source:28
  while len(عقد) > 1:
    # apl-source:29
    # أوجد أقل عقدتين (بفهرسين متميزين)
    # apl-source:30
    أول = -1
    # apl-source:31
    ثان = -1
    # apl-source:32
    for i in range(len(عقد)):
      # apl-source:33
      if أول == -1 or عقد[i][0] < عقد[أول][0]:
        # apl-source:34
        ثان = أول
        # apl-source:35
        أول = i
      # apl-source:36
      elif ثان == -1 or عقد[i][0] < عقد[ثان][0]:
        # apl-source:37
        ثان = i
    # apl-source:38
    # أضف 0 لشيفرات أحرف الأولى و 1 لأحرف الثانية
    # apl-source:39
    for حرف in عقد[أول][1]:
      # apl-source:40
      for i in range(ن):
        # apl-source:41
        if أحرف[i] == حرف:
          # apl-source:42
          شيفرات[i] = "0" + شيفرات[i]
    # apl-source:43
    for حرف in عقد[ثان][1]:
      # apl-source:44
      for i in range(ن):
        # apl-source:45
        if أحرف[i] == حرف:
          # apl-source:46
          شيفرات[i] = "1" + شيفرات[i]
    # apl-source:47
    # ادمج: أزل الأعلى فهرساً أولاً
    # apl-source:48
    تكرار_مجموع = عقد[أول][0] + عقد[ثان][0]
    # apl-source:49
    أحرف_مجموع = عقد[أول][1] + عقد[ثان][1]
    # apl-source:50
    if أول > ثان:
      # apl-source:51
      عقد = عقد[:أول] + عقد[أول + 1:]
      # apl-source:52
      عقد = عقد[:ثان] + عقد[ثان + 1:]
    # apl-source:53
    else:
      # apl-source:54
      عقد = عقد[:ثان] + عقد[ثان + 1:]
      # apl-source:55
      عقد = عقد[:أول] + عقد[أول + 1:]
    # apl-source:56
    عقد = عقد + [[تكرار_مجموع, أحرف_مجموع, ""]]
  # apl-source:57
  return شيفرات
# apl-source:58

# apl-source:59
أحرف = ["a", "b", "c", "d", "e", "f"]
# apl-source:60
تكرارات = [5, 9, 12, 13, 16, 45]
# apl-source:61
شيفرات = هوفمان(أحرف, تكرارات)
# apl-source:62
print("الشيفرات:", شيفرات)
# apl-source:63

# apl-source:64
# f الأكثر تكراراً يأخذ أقصر شيفرة
# apl-source:65
تأكد_يساوي(len(شيفرات[5]), 1, "f بحرف واحد")
# apl-source:66
# خاصية البادئة: لا شيفرة بادئة لأخرى
# apl-source:67
for i in range(6):
  # apl-source:68
  for ج in range(6):
    # apl-source:69
    if i != ج:
      # apl-source:70
      أقصر = شيفرات[i]
      # apl-source:71
      أطول = شيفرات[ج]
      # apl-source:72
      if len(أقصر) <= len(أطول):
        # apl-source:73
        if أطول[:len(أقصر)] == أقصر:
          # apl-source:74
          print("فشل: خاصية البادئة", أقصر, أطول)
          # apl-source:75
          قياسي_نظام_اخرج(1)
# apl-source:76
print("ناجح: خاصية البادئة")
# apl-source:77

# apl-source:78
# الطول المرجح: 5*4+9*4+12*3+13*3+16*3+45*1 = 224
# apl-source:79
طول_مرجح = 0
# apl-source:80
for i in range(6):
  # apl-source:81
  طول_مرجح = طول_مرجح + تكرارات[i] * len(شيفرات[i])
# apl-source:82
print("الطول المرجح:", طول_مرجح)
# apl-source:83
تأكد_يساوي(طول_مرجح, 224, "الطول المرجح الأمثل")
# apl-source:84
