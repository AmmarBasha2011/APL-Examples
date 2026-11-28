# مثال 8001 — أول حرف كبير لكل كلمة في الجملة رقم 10
# caps for sentence 10
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8001-sent9-caps.apl

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

تأكد_يساوي(ف("in the end the end is the start"), "In The End The End Is The Start", "حالة 1")
تأكد_يساوي(ف("cairo is big and cairo is old"), "Cairo Is Big And Cairo Is Old", "حالة 2")
تأكد_يساوي(ف("sun sand sea sun sand sun"), "Sun Sand Sea Sun Sand Sun", "حالة 3")
