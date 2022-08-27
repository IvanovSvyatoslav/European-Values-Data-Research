__dictionary = {8: "Albania", 31: "Azerbaijan", 40: "Austria", 51: "Armenia", 56: "Belgium", 70: "Bosnia and Herzegovina",
              100: "Bulgaria", 112: "Belarus", 191: "Croatia", 196: "Cyprus", 197: "Northern Cyprus",
              203: "Czech Republic", 208: "Denmark", 233: "Estonia", 246: "Finland", 250: "France", 268: "Georgia",
              276: "Germany", 826: "United Kingdom", 300: "Greece", 348: "Hungary", 352: "Iceland", 372: "Ireland",
              380: "Italy", 428: "Latvia", 440: "Lithuania", 442: "Luxembourg", 470: "Malta",
              498: "Republic of Moldova", 499: "Montenegro", 528: "Netherlands",
              807: "The former Yugoslav Republic of Macedonia", 578: "Norway", 616: "Poland", 620: "Portugal",
              642: "Romania", 643: "Russia", 688: "Serbia", 703: "Slovakia", 705: "Slovenia", 724: "Spain",
              752: "Sweden", 756: "Switzerland", 792: "Turkey", 804: "Ukraine", 909: "Northern Ireland", 915: "Kosovo"}


def rename(data: int) -> str:
    return __dictionary.get(data)


def reg(code: int) -> str:
    if code in [8, 70, 191, 499, 807, 688, 705, 792, 915, 300, 197]:
        return 'Balc'
    if code in [380, 620, 724, 470, 196]:
        return 'South'
    if code in [40, 250, 276, 826, 528, 756, 442, 909, 56, 372]:
        return 'West'
    if code in [208, 246, 352, 578, 752]:
        return 'North'
    if code in [100, 112, 203, 348, 616, 642, 643, 703, 498, 804]:
        return 'East'
    if code in [31, 51, 268]:
        return 'Cau'
    if code in [233, 440, 428]:
        return 'Balt'

    return 'Unexpected'


def calc_groups(year: int) -> tuple[list, list, list, list, list, list, list, list]:
    family_group = []
    marriage_group = []
    women_group = []
    children_group = []
    parents_group = []
    lgbt_group = []
    gender = []
    age = []
    # 2017
    if year == 2017:
        family_group += ['v2']
        marriage_group += ['v65', 'v71', 'v155']
        women_group += ['v72', 'v73', 'v74', 'v75']
        children_group += ['v83', 'v69', 'v154']
        parents_group += ['v84']
        lgbt_group += ['v82', 'v153']
        gender += ['v225']
        age += ['age_r3', 'age']
    # 2008
    if year == 2008:
        family_group += ['v2']  # ???
        marriage_group += ['v136', 'v150', 'v242']
        women_group += ['v159', 'v160', 'v161']
        children_group += ['v145', 'v156', 'v241']
        parents_group += ['v167']
        lgbt_group += ['v154', 'v240']
        age += []
        gender += ['v302']
    # 1999
    if year == 1999:
        family_group += ['v2']  # ???
        marriage_group += ['v133', 'v150', 'v234']
        women_group += ['v154', 'v156', 'v99']
        children_group += ['v144', 'v233']
        parents_group += ['v162']
        lgbt_group += ['v232']
        age += []
        gender += ['v291']
    return family_group, marriage_group, women_group, children_group, parents_group, lgbt_group, gender, age


def __from2(val: int) -> int:
    if val == 1:
        return 1
    if val == 2:
        return 10
    return val


def __reversed_from2(val: int) -> int:
    if val == 2:
        return 1
    if val == 1:
        return 10
    return val


def __reversed_from3(val: int) -> int | float:
    if val == 2:
        return 5.5
    if val == 1:
        return 10
    if val == 3:
        return 1
    return val


def __from3(val: int) -> int:
    if val == 2:
        return 5.5
    if val == 3:
        return 10
    return val


def __from4(val: int) -> int:
    if val == 2:
        return 4
    if val == 3:
        return 7
    if val == 4:
        return 10
    return val


def __reversed_from4(val: int) -> int:
    if val == 3:
        return 4
    if val == 2:
        return 7
    if val == 4:
        return 1
    if val == 1:
        return 10
    return val


def __from5(val: int) -> int | float:
    if val == 2:
        return 3.25
    if val == 3:
        return 5.5
    if val == 4:
        return 7.75
    if val == 5:
        return 10
    return val


def __reversed_from5(val: int) -> int | float:
    if val == 3:
        return 3.25
    if val == 2:
        return 5.5
    if val == 2:
        return 7.75
    if val == 1:
        return 10
    if val == 5:
        return 1
    return val


# 2017
def family(data, year: int) -> float:
    if year == 2017:
        summa = 0
        num = 1

        summa += __reversed_from4(data.v2)
        return summa / num
    if year == 2008:
        summa = 0
        num = 1

        summa += __reversed_from4(data.v2)
        return summa / num
    if year == 1999:
        summa = 0
        num = 1

        summa += __reversed_from4(data.v2)
        return summa / num


def marriage(data, year: int) -> float:
    if year == 2017:
        summa = 0
        num = 3

        summa += __from3(data.v65)
        if data.v71 == 2:
            summa += 1
        else:
            summa += 10
        summa += data.v155
        return summa / num
    if year == 2008:
        summa = 0
        num = 3

        summa += __from3(data.v136)
        summa += __reversed_from2(data.v150)
        summa += data.v242
        return summa / num

    if year == 1999:
        summa = 0
        num = 3

        summa += __from3(data.v133)
        summa += __reversed_from2(data.v150)
        summa += data.v234
        return summa / num


def women(data, year: int) -> float:
    if year == 2017:
        summa = 0
        num = 4

        summa += __from4(data.v72)
        summa += __from4(data.v73)
        summa += __from4(data.v74)
        summa += __from4(data.v75)
        return summa / num
    if year == 2008:
        summa = 0
        num = 3

        summa += __reversed_from4(data.v159)
        summa += __from4(data.v160)
        summa += __from4(data.v161)
        return summa / num
    if year == 1999:
        summa = 0
        num = 3

        summa += __from4(data.v154)
        summa += __from4(data.v156)
        summa += __from3(data.v99)
        return summa / num


def children(data, year: int) -> float:
    if year == 2017:
        summa = 0
        num = 3

        summa += __from5(data.v83)
        summa += __from3(data.v69)
        summa += data.v154
        return summa / num
    if year == 2008:
        summa = 0
        num = 3

        summa += __from3(data.v145)
        summa += __from5(data.v156)
        summa += data.v241
        return summa / num
    if year == 1999:
        summa = 0
        num = 2

        summa += __from3(data.v144)
        summa += __from5(data.v233)
        return summa / num


def parents(data, year: int) -> float:
    if year == 2017:
        summa = 0
        num = 1

        summa += __from5(data.v84)
        return summa / num
    if year == 2008:
        summa = 0
        num = 1

        summa += __from2(data.v167)
        return summa / num
    if year == 1999:
        summa = 0
        num = 1

        summa += __from2(data.v162)
        return summa / num


def lgbt(data, year: int) -> float:
    if year == 2017:
        summa = 0
        num = 2

        summa += __from5(data.v82)
        summa += data.v153

        return summa / num
    if year == 2008:
        summa = 0
        num = 2

        summa += __from5(data.v154)
        summa += data.v240

        return summa / num
    if year == 1999:
        summa = 0
        num = 1

        summa += data.v232

        return summa / num
