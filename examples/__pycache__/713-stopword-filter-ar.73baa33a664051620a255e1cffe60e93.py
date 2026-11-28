
# apl-source:1
# مثال 713 — ترشيح كلمات الوقف
# apl-source:2
# Arabic stopword filter
# apl-source:3
# Demonstrates: كلمات وقف، ترشيح، نسبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/713-stopword-filter-ar.apl
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
# ترشيح كلمات الوقف العربية
# apl-source:25
# Demonstrates: قائمة حرفية, ترشيح قائمة, نسبة الإبقاء
# apl-source:26
# الضمائر وحروف الجر وأدوات الربط لا تفيد البحث
# apl-source:27

# apl-source:28
وقف = ["في", "من", "على", "إلى", "عن", "أن", "إن", "كان", "هو", "هي", "هذا", "هذه", "ذلك", "التي", "الذي", "ما", "لا", "لم", "لن", "قد", "ثم", "أو", "و", "يا"]
# apl-source:29

# apl-source:30
def رشح(جملة):
  # apl-source:31
  كلمات = جملة.split(" ")
  # apl-source:32
  ناتج = []
  # apl-source:33
  for ك in كلمات:
    # apl-source:34
    if (ك in وقف) == False and len(ك) > 0:
      # apl-source:35
      ناتج.append(ك)
  # apl-source:36
  return ناتج
# apl-source:37

# apl-source:38
def نسبة(أصلية, مبقاة):
  # apl-source:39
  return len(مبقاة) * 100 // len(أصلية)
# apl-source:40

# apl-source:41
ك1 = رشح("ذهب الولد إلى المدرسة في الصباح")
# apl-source:42
تأكد_يساوي(ك1, ["ذهب", "الولد", "المدرسة", "الصباح"], "حذف إلى وفي")
# apl-source:43
ك2 = رشح("هذا هو الكتاب الذي قرأته")
# apl-source:44
تأكد_يساوي(ك2, ["الكتاب", "قرأته"], "ضمائر وأدوات موصول")
# apl-source:45
تأكد_يساوي(رشح(""), [], "جملة فارغة")
# apl-source:46
ك4 = رشح("البرمجة ممتعة والتعلم مستمر")
# apl-source:47
تأكد_يساوي(len(ك4), 4, "لا وقف هنا تقريبا")
# apl-source:48
تأكد_يساوي(نسبة("ذهب الولد إلى المدرسة في الصباح".split(" "), ك1), 66, "نسبة الإبقاء")
# apl-source:49
print(ك1)
# apl-source:50
