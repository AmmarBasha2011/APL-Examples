# مثال 7902 — تكرار كل كلمة في الجملة رقم 1
# freq for sentence 1
# Demonstrates: متتاليات ومعالجة
#
# Run:  python apl.py examples/7902-sent0-freq.apl

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
    د[ك] = د.get(ك, 0) + 1
  ارجع د

تأكد_يساوي(ف("the cat and the dog and the bird"), {"the": 3, "cat": 1, "and": 2, "dog": 1, "bird": 1}, "حالة 1")
تأكد_يساوي(ف("one fish two fish red fish blue fish"), {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1}, "حالة 2")
تأكد_يساوي(ف("run run run fast fast slow"), {"run": 3, "fast": 2, "slow": 1}, "حالة 3")
