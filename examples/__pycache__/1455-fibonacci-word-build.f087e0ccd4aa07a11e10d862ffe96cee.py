
# apl-source:1
# مثال 1455 — كلمة فيبوناتشي
# apl-source:2
# Fibonacci word construction
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1455-fibonacci-word-build.apl
# apl-source:6

# apl-source:7
# نبدأ بـ a ثم ab
# apl-source:8
# كل كلمة هي السابقة مضافاً إليها ما قبلها
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def كلمة_فيبو(ن):
  # apl-source:19
  if ن == 1:
    # apl-source:20
    return "a"
  # apl-source:21
  سابق = "a"
  # apl-source:22
  حالي = "ab"
  # apl-source:23
  for ع in range(2, ن):
    # apl-source:24
    تالي = حالي + سابق
    # apl-source:25
    سابق = حالي
    # apl-source:26
    حالي = تالي
  # apl-source:27
  return حالي
# apl-source:28

# apl-source:29
تأكد_يساوي(كلمة_فيبو(1), "a", "أولى")
# apl-source:30
تأكد_يساوي(كلمة_فيبو(2), "ab", "ثانية")
# apl-source:31
تأكد_يساوي(كلمة_فيبو(4), "abaab", "رابعة")
# apl-source:32
تأكد_يساوي(len(كلمة_فيبو(7)), 21, "طول سابعة")
# apl-source:33
