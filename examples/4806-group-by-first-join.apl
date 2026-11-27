# مثال 4806 — تجميع الكلمات حسب الحرف الأول (الكلمات)
# Group words by first letter: words
# Demonstrates: قواميس وتجميع
#
# Run:  python apl.py examples/4806-group-by-first-join.apl

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
    ك = خ[0]
    لو ك في د:
      د[ك] = د[ك] + [خ]
    والا:
      د[ك] = [خ]
  ارجع د

تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {"a": ["apple", "apricot", "axe"], "b": ["bob", "bear"], "c": ["cat"], "d": ["dog"]}, "حالة 1")
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {"s": ["sun", "star", "sky"], "m": ["moon", "mars"]}, "حالة 2")
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {"o": ["one"], "t": ["two", "three"], "f": ["four", "five"], "s": ["six"]}, "حالة 3")
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {"k": ["kiwi", "kale"], "l": ["lime", "lemon", "leek"]}, "حالة 4")
