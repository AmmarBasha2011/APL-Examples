# مثال 4803 — تجميع الكلمات حسب الطول (الكلمات)
# Group words by length: words
# Demonstrates: قواميس وتجميع
#
# Run:  python apl.py examples/4803-group-by-length-join.apl

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
    ك = len(خ)
    لو ك في د:
      د[ك] = د[ك] + [خ]
    والا:
      د[ك] = [خ]
  ارجع د

تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {5: ["apple"], 3: ["bob", "cat", "dog", "axe"], 7: ["apricot"], 4: ["bear"]}, "حالة 1")
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {3: ["sun", "sky"], 4: ["moon", "star", "mars"]}, "حالة 2")
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {3: ["one", "two", "six"], 5: ["three"], 4: ["four", "five"]}, "حالة 3")
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {4: ["kiwi", "lime", "kale", "leek"], 5: ["lemon"]}, "حالة 4")
