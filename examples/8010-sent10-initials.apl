# مثال 8010 — الحروف الأولى في الجملة رقم 11
# initials for sentence 11
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8010-sent10-initials.apl

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

تأكد_يساوي(ف("red blue green red blue red"), "rbgrbr", "حالة 1")
تأكد_يساوي(ف("nile river nile delta river"), "nrndr", "حالة 2")
تأكد_يساوي(ف("bread milk bread eggs milk bread"), "bmbemb", "حالة 3")
