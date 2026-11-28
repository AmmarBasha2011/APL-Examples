# مثال 8051 — أول حرف كبير لكل كلمة في الجملة رقم 15
# caps for sentence 15
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8051-sent14-caps.apl

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

تأكد_يساوي(ف("learn code learn more code more"), "Learn Code Learn More Code More", "حالة 1")
تأكد_يساوي(ف("bread milk bread eggs milk bread"), "Bread Milk Bread Eggs Milk Bread", "حالة 2")
تأكد_يساوي(ف("to be or not to be"), "To Be Or Not To Be", "حالة 3")
