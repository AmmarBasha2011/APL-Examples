# مثال 8021 — أول حرف كبير لكل كلمة في الجملة رقم 12
# caps for sentence 12
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8021-sent11-caps.apl

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

تأكد_يساوي(ف("up down up down up up down"), "Up Down Up Down Up Up Down", "حالة 1")
تأكد_يساوي(ف("learn code learn more code more"), "Learn Code Learn More Code More", "حالة 2")
تأكد_يساوي(ف("left right left left right"), "Left Right Left Left Right", "حالة 3")
