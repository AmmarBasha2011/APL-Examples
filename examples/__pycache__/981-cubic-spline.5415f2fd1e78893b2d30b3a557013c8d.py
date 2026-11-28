
# apl-source:1
# مثال 981 — السبلين التكعيبي
# apl-source:2
# Cubic spline
# apl-source:3
# Demonstrates: ثلاثي القطر بتوماس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/981-cubic-spline.apl
# apl-source:6

# apl-source:7
# السبلين التكعيبي الطبيعي: منحنى أملس يمر بالنقاط بمشتقتين متصلتين
# apl-source:8
# حل نظام ثلاثي القطر بخوارزمية توماس
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
def حل_ثلاثي(أ, ب, ج, د, ن):
  # apl-source:19
  ب2 = []
  # apl-source:20
  د2 = []
  # apl-source:21
  for i in range(ن):
    # apl-source:22
    ب2 = ب2 + [ب[i]]
    # apl-source:23
    د2 = د2 + [د[i]]
  # apl-source:24
  for i in range(1, ن):
    # apl-source:25
    وزن = أ[i] / ب2[i - 1]
    # apl-source:26
    ب2[i] = ب2[i] - (وزن * ج[i - 1])
    # apl-source:27
    د2[i] = د2[i] - (وزن * د2[i - 1])
  # apl-source:28
  م = []
  # apl-source:29
  for i in range(ن):
    # apl-source:30
    م = م + [0]
  # apl-source:31
  م[ن - 1] = د2[ن - 1] / ب2[ن - 1]
  # apl-source:32
  for i in range(ن - 2, -1, -1):
    # apl-source:33
    م[i] = (د2[i] - (ج[i] * م[i + 1])) / ب2[i]
  # apl-source:34
  return م
# apl-source:35

# apl-source:36
نقاط_س = [0, 1, 2, 3]
# apl-source:37
نقاط_ص = [0, 1, 0, 1]
# apl-source:38
ن = 4
# apl-source:39
ح = []
# apl-source:40
for i in range(ن - 1):
  # apl-source:41
  ح = ح + [نقاط_س[i + 1] - نقاط_س[i]]
# apl-source:42
أ = [0, 0, 0, 0]
# apl-source:43
ب = [1, 0, 0, 1]
# apl-source:44
ج = [0, 0, 0, 0]
# apl-source:45
د = [0, 0, 0, 0]
# apl-source:46
for i in range(1, ن - 1):
  # apl-source:47
  أ[i] = ح[i - 1]
  # apl-source:48
  ب[i] = 2 * (ح[i - 1] + ح[i])
  # apl-source:49
  ج[i] = ح[i]
  # apl-source:50
  د[i] = 6 * (((نقاط_ص[i + 1] - نقاط_ص[i]) / ح[i]) - ((نقاط_ص[i] - نقاط_ص[i - 1]) / ح[i - 1]))
# apl-source:51

# apl-source:52
م = حل_ثلاثي(أ, ب, ج, د, ن)
# apl-source:53

# apl-source:54
def قيم(س):
  # apl-source:55
  i = 0
  # apl-source:56
  while (i < (ن - 2)) and (س > نقاط_س[i + 1]):
    # apl-source:57
    i = i + 1
  # apl-source:58
  عرض = نقاط_س[i + 1] - نقاط_س[i]
  # apl-source:59
  آ = (نقاط_س[i + 1] - س) / عرض
  # apl-source:60
  بق = (س - نقاط_س[i]) / عرض
  # apl-source:61
  حد1 = (آ * نقاط_ص[i]) + (بق * نقاط_ص[i + 1])
  # apl-source:62
  حد2 = ((((آ * آ * آ) - آ) * م[i]) + (((بق * بق * بق) - بق) * م[i + 1])) * عرض * عرض / 6
  # apl-source:63
  return حد1 + حد2
# apl-source:64

# apl-source:65
تأكد_يساوي(round(م[0], 6), 0, "طبيعي عند الطرف")
# apl-source:66
تأكد_يساوي(round(م[1], 6), -4, "الانحناء الأول")
# apl-source:67
تأكد_يساوي(round(م[2], 6), 4, "الانحناء الثاني")
# apl-source:68
تأكد_يساوي(round(قيم(0.5), 6), 0.75, "تقييم عند النصف")
# apl-source:69
تأكد_يساوي(round(قيم(1.5), 6), 0.5, "تقييم عند الواحد ونصف")
# apl-source:70
تأكد_يساوي(round(قيم(2), 6), 0, "يمر بالنقاط")
# apl-source:71
