# مثال 7909 — أول كلمة تتكرر في الجملة رقم 1
# firstdup for sentence 1
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7909-sent0-firstdup.apl

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
  د = {}
  لكل ك في ن.split(" "):
    لو ك في د:
      ارجع ك
    د[ك] = 1
  ارجع ""

تأكد_يساوي(ف("the cat and the dog and the bird"), "the", "حالة 1")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), "fish", "حالة 2")
تأكد_يساوي(ف("run run run fast fast slow"), "run", "حالة 3")
