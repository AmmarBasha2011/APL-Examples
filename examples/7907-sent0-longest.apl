# مثال 7907 — أطول كلمة (الأولى عند التساوي) في الجملة رقم 1
# longest for sentence 1
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7907-sent0-longest.apl

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

تأكد_يساوي(ف("the cat and the dog and the bird"), "bird", "حالة 1")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), "fish", "حالة 2")
تأكد_يساوي(ف("run run run fast fast slow"), "fast", "حالة 3")
