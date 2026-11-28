# مثال 8041 — أول حرف كبير لكل كلمة في الجملة رقم 14
# caps for sentence 14
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8041-sent13-caps.apl

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

تأكد_يساوي(ف("nile river nile delta river"), "Nile River Nile Delta River", "حالة 1")
تأكد_يساوي(ف("sun sand sea sun sand sun"), "Sun Sand Sea Sun Sand Sun", "حالة 2")
تأكد_يساوي(ف("the cat and the dog and the bird"), "The Cat And The Dog And The Bird", "حالة 3")
