
# apl-source:1
# مثال 919 — متتابعة فان إك
# apl-source:2
# Van Eck sequence
# apl-source:3
# Demonstrates: عمر آخر ظهور
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/919-van-eck.apl
# apl-source:6

# apl-source:7
# متتابعة فان إك: الحد التالي هو عمر الحد الحالي
# apl-source:8
# صفر إن ظهر لأول مرة، وإلا الفرق بين آخر ظهورين
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
def فان_إك(عدد):
  # apl-source:19
  أ = [0]
  # apl-source:20
  for i in range(1, عدد):
    # apl-source:21
    أخير = أ[len(أ) - 1]
    # apl-source:22
    # ابحث عن آخر ظهور سابق (ليس الموضع الأخير)
    # apl-source:23
    سابق = -1
    # apl-source:24
    ج = len(أ) - 2
    # apl-source:25
    while ج >= 0:
      # apl-source:26
      if أ[ج] == أخير and سابق == -1:
        # apl-source:27
        سابق = ج
      # apl-source:28
      ج = ج - 1
    # apl-source:29
    if سابق == -1:
      # apl-source:30
      أ = أ + [0]
    # apl-source:31
    else:
      # apl-source:32
      أ = أ + [len(أ) - 1 - سابق]
  # apl-source:33
  return أ
# apl-source:34

# apl-source:35
أ = فان_إك(12)
# apl-source:36
print("أول 12 حداً:", أ)
# apl-source:37

# apl-source:38
متوقع = [0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5]
# apl-source:39
تأكد_يساوي(len(أ), 12, "الطول")
# apl-source:40
for i in range(12):
  # apl-source:41
  تأكد_يساوي(أ[i], متوقع[i], "حد " + str(i))
# apl-source:42
