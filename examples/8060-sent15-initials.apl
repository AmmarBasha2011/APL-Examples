# مثال 8060 — الحروف الأولى في الجملة رقم 16
# initials for sentence 16
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8060-sent15-initials.apl

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

تأكد_يساوي(ف("stars and moon and stars again"), "samasa", "حالة 1")
تأكد_يساوي(ف("left right left left right"), "lrllr", "حالة 2")
تأكد_يساوي(ف("apl code is easy code is fun"), "aciecif", "حالة 3")
