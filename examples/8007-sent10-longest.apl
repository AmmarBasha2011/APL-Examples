# مثال 8007 — أطول كلمة (الأولى عند التساوي) في الجملة رقم 11
# longest for sentence 11
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8007-sent10-longest.apl

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
    لو len(ك) > len(ر):
      ر = ك
  ارجع ر

تأكد_يساوي(ف("red blue green red blue red"), "green", "حالة 1")
تأكد_يساوي(ف("nile river nile delta river"), "river", "حالة 2")
تأكد_يساوي(ف("bread milk bread eggs milk bread"), "bread", "حالة 3")
