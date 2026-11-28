# مثال 8020 — الحروف الأولى في الجملة رقم 12
# initials for sentence 12
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8020-sent11-initials.apl

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

تأكد_يساوي(ف("up down up down up up down"), "ududuud", "حالة 1")
تأكد_يساوي(ف("learn code learn more code more"), "lclmcm", "حالة 2")
تأكد_يساوي(ف("left right left left right"), "lrllr", "حالة 3")
