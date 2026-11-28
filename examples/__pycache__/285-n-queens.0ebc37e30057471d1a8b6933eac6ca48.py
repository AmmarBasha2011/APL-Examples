
# apl-source:1
# مثال 285 — ملكات الشطرنج (عد الحلول)
# apl-source:2
# N-Queens (count solutions)
# apl-source:3
# Demonstrates: تراجع مع فحص الأعمدة والأقطار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/285-n-queens.apl
# apl-source:6

# apl-source:7
def آمن(صفوف, رقم_الصف, عمود):
    # apl-source:8
    for سابق in range(رقم_الصف):
        # apl-source:9
        عمود_سابق = صفوف[سابق]
        # apl-source:10
        if عمود_سابق == عمود:
            # apl-source:11
            return False
        # apl-source:12
        فرق = عمود_سابق - عمود
        # apl-source:13
        if فرق < 0:
            # apl-source:14
            فرق = -فرق
        # apl-source:15
        if فرق == رقم_الصف - سابق:
            # apl-source:16
            return False
    # apl-source:17
    return True
# apl-source:18

# apl-source:19
def حل_ملكات(ن, رقم_الصف, صفوف, عداد):
    # apl-source:20
    if رقم_الصف == ن:
        # apl-source:21
        عداد["عدد"] = عداد["عدد"] + 1
        # apl-source:22
        return
    # apl-source:23
    for عمود in range(ن):
        # apl-source:24
        if آمن(صفوف, رقم_الصف, عمود):
            # apl-source:25
            صفوف.append(عمود)
            # apl-source:26
            حل_ملكات(ن, رقم_الصف + 1, صفوف, عداد)
            # apl-source:27
            صفوف.pop()
# apl-source:28

# apl-source:29
def عد_الحلول(ن):
    # apl-source:30
    عداد = {"عدد": 0}
    # apl-source:31
    حل_ملكات(ن, 0, [], عداد)
    # apl-source:32
    return عداد["عدد"]
# apl-source:33

# apl-source:34
print("حلول 4x4:", عد_الحلول(4))
# apl-source:35
print("حلول 6x6:", عد_الحلول(6))
# apl-source:36
print("حلول 8x8:", عد_الحلول(8))
# apl-source:37
