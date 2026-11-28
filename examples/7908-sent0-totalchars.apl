# مثال 7908 — مجموع حروف الكلمات في الجملة رقم 1
# totalchars for sentence 1
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7908-sent0-totalchars.apl

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
  م = 0
  لكل ك في ن.split(" "):
    م = م + len(ك)
  ارجع م

تأكد_يساوي(ف("the cat and the dog and the bird"), 25, "حالة 1")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), 29, "حالة 2")
تأكد_يساوي(ف("run run run fast fast slow"), 21, "حالة 3")
