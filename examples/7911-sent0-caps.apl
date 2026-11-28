# مثال 7911 — أول حرف كبير لكل كلمة في الجملة رقم 1
# caps for sentence 1
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7911-sent0-caps.apl

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
  ر = []
  لكل ك في ن.split(" "):
    ر = ر + [ك[0].upper() + ك[1:]]
  ارجع " ".join(ر)

تأكد_يساوي(ف("the cat and the dog and the bird"), "The Cat And The Dog And The Bird", "حالة 1")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), "One Fish Two Fish Red Fish Blue Fish", "حالة 2")
تأكد_يساوي(ف("run run run fast fast slow"), "Run Run Run Fast Fast Slow", "حالة 3")
