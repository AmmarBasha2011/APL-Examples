# مثال 8080 — الحروف الأولى في الجملة رقم 18
# initials for sentence 18
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8080-sent17-initials.apl

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

تأكد_يساوي(ف("bread milk bread eggs milk bread"), "bmbemb", "حالة 1")
تأكد_يساوي(ف("the cat and the dog and the bird"), "tcatdatb", "حالة 2")
تأكد_يساوي(ف("a rose is a rose is a rose"), "ariariar", "حالة 3")
