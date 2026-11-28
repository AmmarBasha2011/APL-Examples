# مثال 8071 — أول حرف كبير لكل كلمة في الجملة رقم 17
# caps for sentence 17
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8071-sent16-caps.apl

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

تأكد_يساوي(ف("sun sand sea sun sand sun"), "Sun Sand Sea Sun Sand Sun", "حالة 1")
تأكد_يساوي(ف("yes no yes yes no maybe"), "Yes No Yes Yes No Maybe", "حالة 2")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), "One Fish Two Fish Red Fish Blue Fish", "حالة 3")
