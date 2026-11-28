# مثال 7927 — أطول كلمة (الأولى عند التساوي) في الجملة رقم 3
# longest for sentence 3
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7927-sent2-longest.apl

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

تأكد_يساوي(ف("apl code is easy code is fun"), "code", "حالة 1")
تأكد_يساوي(ف("we love data and data loves us"), "loves", "حالة 2")
تأكد_يساوي(ف("in the end the end is the start"), "start", "حالة 3")
