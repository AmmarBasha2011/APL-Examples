
# apl-source:1
# مثال 587 — مخزن دائري
# apl-source:2
# Circular buffer
# apl-source:3
# Demonstrates: مخزن دائري، كتابة فوق، سعة ثابتة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/587-circular-buffer.apl
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
# مخزن دائري (ring buffer) بحجم ثابت
# apl-source:25
# Demonstrates: كتابة تلف حول مصفوفة, استهلاك بالترتيب, كشف الامتلاء
# apl-source:26
# يستخدم في تدفقات البيانات والسجلات
# apl-source:27

# apl-source:28
def أنشئ_مخزن(سعة):
  # apl-source:29
  return {"عناصر": [0] * سعة, "رأس": 0, "ذيل": 0, "عدد": 0, "سعة": سعة}
# apl-source:30

# apl-source:31
def ادفع(م, قيمة):
  # apl-source:32
  م["عناصر"][م["ذيل"]] = قيمة
  # apl-source:33
  م["ذيل"] = (م["ذيل"] + 1) % م["سعة"]
  # apl-source:34
  if م["عدد"] < م["سعة"]:
    # apl-source:35
    م["عدد"] = م["عدد"] + 1
  # apl-source:36
  else:
    # apl-source:37
    م["رأس"] = (م["رأس"] + 1) % م["سعة"]
# apl-source:38

# apl-source:39
def اسحب(م):
  # apl-source:40
  قيمة = م["عناصر"][م["رأس"]]
  # apl-source:41
  م["رأس"] = (م["رأس"] + 1) % م["سعة"]
  # apl-source:42
  م["عدد"] = م["عدد"] - 1
  # apl-source:43
  return قيمة
# apl-source:44

# apl-source:45
م = أنشئ_مخزن(3)
# apl-source:46
ادفع(م, 10)
# apl-source:47
ادفع(م, 20)
# apl-source:48
ادفع(م, 30)
# apl-source:49
ادفع(م, 40)
# apl-source:50
print("عدد العناصر:", م["عدد"])
# apl-source:51
تأكد_يساوي(م["عدد"], 3, "السعة القصوى محفوظة")
# apl-source:52
تأكد_يساوي(اسحب(م), 20, "أقدم عنصر بعد الكتابة فوق 10")
# apl-source:53
ادفع(م, 50)
# apl-source:54
تأكد_يساوي(اسحب(م), 30, "ترتيب الاستهلاك 1")
# apl-source:55
تأكد_يساوي(اسحب(م), 40, "ترتيب الاستهلاك 2")
# apl-source:56
تأكد_يساوي(اسحب(م), 50, "ترتيب الاستهلاك 3")
# apl-source:57
تأكد_يساوي(م["عدد"], 0, "فارغ في النهاية")
# apl-source:58
