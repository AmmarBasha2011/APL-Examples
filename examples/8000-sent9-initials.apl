# مثال 8000 — الحروف الأولى في الجملة رقم 10
# initials for sentence 10
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8000-sent9-initials.apl

# نقسم الجملة إلى كلمات
# ونعالجها حسب المطلوب

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = ""
  لكل ك في ن.split(" "):
    ر = ر + ك[0]
  ارجع ر

تأكد_يساوي(ف("in the end the end is the start"), "iteteits", "حالة 1")
تأكد_يساوي(ف("cairo is big and cairo is old"), "cibacio", "حالة 2")
تأكد_يساوي(ف("sun sand sea sun sand sun"), "ssssss", "حالة 3")
