# مثال 8040 — الحروف الأولى في الجملة رقم 14
# initials for sentence 14
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8040-sent13-initials.apl

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

تأكد_يساوي(ف("nile river nile delta river"), "nrndr", "حالة 1")
تأكد_يساوي(ف("sun sand sea sun sand sun"), "ssssss", "حالة 2")
تأكد_يساوي(ف("the cat and the dog and the bird"), "tcatdatb", "حالة 3")
