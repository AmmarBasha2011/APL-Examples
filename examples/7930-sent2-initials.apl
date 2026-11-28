# مثال 7930 — الحروف الأولى في الجملة رقم 3
# initials for sentence 3
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7930-sent2-initials.apl

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

تأكد_يساوي(ف("apl code is easy code is fun"), "aciecif", "حالة 1")
تأكد_يساوي(ف("we love data and data loves us"), "wldadlu", "حالة 2")
تأكد_يساوي(ف("in the end the end is the start"), "iteteits", "حالة 3")
