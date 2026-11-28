
# apl-source:1
# مثال 995 — المخزن الحلقي
# apl-source:2
# Ring buffer
# apl-source:3
# Demonstrates: مؤشران يلفان بباقي القسمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/995-ring-buffer.apl
# apl-source:6

# apl-source:7
# المخزن الحلقي: طابور بسعة ثابتة يلف مؤشراه على المصفوفة
# apl-source:8
# الكتابة فوق الأقدم عند الامتلاء سلوك معروف
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
سعة = 3
# apl-source:19
حلقة = [0, 0, 0]
# apl-source:20
رأس = [0]
# apl-source:21
ذيل = [0]
# apl-source:22
حجم = [0]
# apl-source:23

# apl-source:24
def ادفع(قيمة):
  # apl-source:25
  حلقة[ذيل[0]] = قيمة
  # apl-source:26
  ذيل[0] = (ذيل[0] + 1) % سعة
  # apl-source:27
  if حجم[0] < سعة:
    # apl-source:28
    حجم[0] = حجم[0] + 1
  # apl-source:29
  else:
    # apl-source:30
    رأس[0] = (رأس[0] + 1) % سعة
  # apl-source:31
  return 0
# apl-source:32

# apl-source:33
def اسحب():
  # apl-source:34
  قيمة = حلقة[رأس[0]]
  # apl-source:35
  رأس[0] = (رأس[0] + 1) % سعة
  # apl-source:36
  حجم[0] = حجم[0] - 1
  # apl-source:37
  return قيمة
# apl-source:38

# apl-source:39
ادفع(1)
# apl-source:40
ادفع(2)
# apl-source:41
ادفع(3)
# apl-source:42
تأكد_يساوي(اسحب(), 1, "الأقدم أولاً")
# apl-source:43
ادفع(4)
# apl-source:44
تأكد_يساوي(اسحب(), 2, "بعد اللف")
# apl-source:45
تأكد_يساوي(حجم[0], 2, "عنصران متبقيان")
# apl-source:46
ادفع(5)
# apl-source:47
ادفع(6)
# apl-source:48
تأكد_يساوي(اسحب(), 4, "تجاوز الكتابة")
# apl-source:49
تأكد_يساوي(اسحب(), 5, "الترتيب محفوظ")
# apl-source:50
