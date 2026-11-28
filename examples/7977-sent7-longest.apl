# مثال 7977 — أطول كلمة (الأولى عند التساوي) في الجملة رقم 8
# longest for sentence 8
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7977-sent7-longest.apl

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

تأكد_يساوي(ف("run run run fast fast slow"), "fast", "حالة 1")
تأكد_يساوي(ف("red blue green red blue red"), "green", "حالة 2")
تأكد_يساوي(ف("learn code learn more code more"), "learn", "حالة 3")
