
# apl-source:1
# مثال 841 — خوارزمية توماس
# apl-source:2
# Thomas algorithm
# apl-source:3
# Demonstrates: مسح أمامي وخلفي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/841-thomas-tridiagonal.apl
# apl-source:6

# apl-source:7
# خوارزمية توماس: حل أنظمة ثلاثية القطر في زمن خطي O(n)
# apl-source:8
# حالة خاصة من الحذف الجاوسي للمصفوفات النطاقية
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
# تحت القطر: أ[1..ن-1]، القطر: ب، فوق القطر: ج[0..ن-2]، الطرف: د
# apl-source:19
def توماس(أ, ب, ج, د):
  # apl-source:20
  ن = len(ب)
  # apl-source:21
  جـ = []
  # apl-source:22
  دـ = []
  # apl-source:23
  جـ = جـ + [ج[0] / ب[0]]
  # apl-source:24
  دـ = دـ + [د[0] / ب[0]]
  # apl-source:25
  for i in range(1, ن):
    # apl-source:26
    مقام = ب[i] - أ[i] * جـ[i - 1]
    # apl-source:27
    if i < ن - 1:
      # apl-source:28
      جـ = جـ + [ج[i] / مقام]
    # apl-source:29
    دـ = دـ + [(د[i] - أ[i] * دـ[i - 1]) / مقام]
  # apl-source:30
  حل = []
  # apl-source:31
  for _ in range(ن):
    # apl-source:32
    حل = حل + [0.0]
  # apl-source:33
  حل[ن - 1] = دـ[ن - 1]
  # apl-source:34
  for i in range(1, ن):
    # apl-source:35
    ت = ن - 1 - i
    # apl-source:36
    حل[ت] = دـ[ت] - جـ[ت] * حل[ت + 1]
  # apl-source:37
  return حل
# apl-source:38

# apl-source:39
# النظام: 2x+ y=4 ، x+2y+ z=4 ، y+2z=4  =>  x=2 ، y=0 ، z=2
# apl-source:40
حل = توماس(
  # apl-source:41
  [0.0, 1.0, 1.0],
  # apl-source:42
  [2.0, 2.0, 2.0],
  # apl-source:43
  [1.0, 1.0, 0.0],
  # apl-source:44
  [4.0, 4.0, 4.0]
# apl-source:45
)
# apl-source:46
print("الحل =", حل)
# apl-source:47

# apl-source:48
تأكد_يساوي(round(حل[0], 9), 2.0, "س = 2")
# apl-source:49
تأكد_يساوي(round(حل[1], 9), 0.0, "ص = 0")
# apl-source:50
تأكد_يساوي(round(حل[2], 9), 2.0, "ع = 2")
# apl-source:51

# apl-source:52
# تحقق بالتعويض المباشر في المعادلات الثلاث
# apl-source:53
تحقق1 = 2.0*حل[0] + 1.0*حل[1]
# apl-source:54
تحقق2 = 1.0*حل[0] + 2.0*حل[1] + 1.0*حل[2]
# apl-source:55
تحقق3 = 1.0*حل[1] + 2.0*حل[2]
# apl-source:56
تأكد_يساوي(round(تحقق1, 9), 4.0, "المعادلة الأولى")
# apl-source:57
تأكد_يساوي(round(تحقق2, 9), 4.0, "المعادلة الثانية")
# apl-source:58
تأكد_يساوي(round(تحقق3, 9), 4.0, "المعادلة الثالثة")
# apl-source:59
