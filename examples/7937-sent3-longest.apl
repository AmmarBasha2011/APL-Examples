# مثال 7937 — أطول كلمة (الأولى عند التساوي) في الجملة رقم 4
# longest for sentence 4
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7937-sent3-longest.apl

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

تأكد_يساوي(ف("one fish two fish red fish blue fish"), "fish", "حالة 1")
تأكد_يساوي(ف("tea for two and two for tea"), "tea", "حالة 2")
تأكد_يساوي(ف("red blue green red blue red"), "green", "حالة 3")
