# مثال 8100 — الحروف الأولى في الجملة رقم 20
# initials for sentence 20
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8100-sent19-initials.apl

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

تأكد_يساوي(ف("yes no yes yes no maybe"), "ynyynm", "حالة 1")
تأكد_يساوي(ف("apl code is easy code is fun"), "aciecif", "حالة 2")
تأكد_يساوي(ف("tea for two and two for tea"), "tftatft", "حالة 3")
