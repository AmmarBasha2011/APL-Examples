# مثال 7951 — أول حرف كبير لكل كلمة في الجملة رقم 5
# caps for sentence 5
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7951-sent4-caps.apl

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

تأكد_يساوي(ف("a rose is a rose is a rose"), "A Rose Is A Rose Is A Rose", "حالة 1")
تأكد_يساوي(ف("run run run fast fast slow"), "Run Run Run Fast Fast Slow", "حالة 2")
تأكد_يساوي(ف("up down up down up up down"), "Up Down Up Down Up Up Down", "حالة 3")
