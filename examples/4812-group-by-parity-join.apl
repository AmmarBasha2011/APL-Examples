# مثال 4812 — تجميع الكلمات حسب زوجية الطول (الكلمات)
# Group words by length parity: words
# Demonstrates: قواميس وتجميع
#
# Run:  python apl.py examples/4812-group-by-parity-join.apl

# نمر على الكلمات
# ونحدّث القاموس حسب المفتاح

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ق):
  د = {}
  لكل خ في ق:
    ك = len(خ) % 2
    لو ك في د:
      د[ك] = د[ك] + [خ]
    والا:
      د[ك] = [خ]
  ارجع د

تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {1: ["apple", "bob", "cat", "apricot", "dog", "axe"], 0: ["bear"]}, "حالة 1")
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {1: ["sun", "sky"], 0: ["moon", "star", "mars"]}, "حالة 2")
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {1: ["one", "two", "three", "six"], 0: ["four", "five"]}, "حالة 3")
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {0: ["kiwi", "lime", "kale", "leek"], 1: ["lemon"]}, "حالة 4")
