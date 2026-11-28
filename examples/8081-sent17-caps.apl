# مثال 8081 — أول حرف كبير لكل كلمة في الجملة رقم 18
# caps for sentence 18
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/8081-sent17-caps.apl

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

تأكد_يساوي(ف("bread milk bread eggs milk bread"), "Bread Milk Bread Eggs Milk Bread", "حالة 1")
تأكد_يساوي(ف("the cat and the dog and the bird"), "The Cat And The Dog And The Bird", "حالة 2")
تأكد_يساوي(ف("a rose is a rose is a rose"), "A Rose Is A Rose Is A Rose", "حالة 3")
