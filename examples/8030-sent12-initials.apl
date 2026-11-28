# مثال 8030 — الحروف الأولى في الجملة رقم 13
# initials for sentence 13
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8030-sent12-initials.apl

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

تأكد_يساوي(ف("cairo is big and cairo is old"), "cibacio", "حالة 1")
تأكد_يساوي(ف("stars and moon and stars again"), "samasa", "حالة 2")
تأكد_يساوي(ف("yes no yes yes no maybe"), "ynyynm", "حالة 3")
