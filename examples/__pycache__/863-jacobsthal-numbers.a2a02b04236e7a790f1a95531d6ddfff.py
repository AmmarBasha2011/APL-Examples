
# apl-source:1
# مثال 863 — أعداد جاكوبستال
# apl-source:2
# Jacobsthal numbers
# apl-source:3
# Demonstrates: J(n)=J(n-1)+2J(n-2)
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/863-jacobsthal-numbers.apl
# apl-source:6

# apl-source:7
# أعداد جاكوبستال: J(n) = J(n-1) + 2*J(n-2) تبدأ 0, 1
# apl-source:8
# تظهر في تبليط الشبكات وعد تغطيات الدومينو
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
def جاكوبستال(ن):
  # apl-source:19
  أ = 0
  # apl-source:20
  ب = 1
  # apl-source:21
  for _ in range(ن):
    # apl-source:22
    جديد = ب + 2 * أ
    # apl-source:23
    أ = ب
    # apl-source:24
    ب = جديد
  # apl-source:25
  return أ
# apl-source:26

# apl-source:27
print("J0..J10:", [جاكوبستال(0), جاكوبستال(1), جاكوبستال(2), جاكوبستال(3), جاكوبستال(4), جاكوبستال(5), جاكوبستال(6), جاكوبستال(7), جاكوبستال(8), جاكوبستال(9), جاكوبستال(10)])
# apl-source:28

# apl-source:29
تأكد_يساوي(جاكوبستال(0), 0, "J0 = 0")
# apl-source:30
تأكد_يساوي(جاكوبستال(3), 3, "J3 = 3")
# apl-source:31
تأكد_يساوي(جاكوبستال(7), 43, "J7 = 43")
# apl-source:32
تأكد_يساوي(جاكوبستال(10), 341, "J10 = 341")
# apl-source:33

# apl-source:34
# صيغة مغلقة: J(n) = (2^n - (-1)^n) / 3
# apl-source:35
قوة2 = 1
# apl-source:36
إشارة = 1
# apl-source:37
for ن in range(0, 10):
  # apl-source:38
  مغلقة = (قوة2 - إشارة) // 3
  # apl-source:39
  تأكد_يساوي(جاكوبستال(ن), مغلقة, "الصيغة المغلقة عند " + str(ن))
  # apl-source:40
  قوة2 = قوة2 * 2
  # apl-source:41
  إشارة = -إشارة
# apl-source:42
