# مثال 7981 — أول حرف كبير لكل كلمة في الجملة رقم 8
# caps for sentence 8
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7981-sent7-caps.apl

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

تأكد_يساوي(ف("run run run fast fast slow"), "Run Run Run Fast Fast Slow", "حالة 1")
تأكد_يساوي(ف("red blue green red blue red"), "Red Blue Green Red Blue Red", "حالة 2")
تأكد_يساوي(ف("learn code learn more code more"), "Learn Code Learn More Code More", "حالة 3")
