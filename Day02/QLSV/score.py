def calculate_average(math, english, physics):
    return (math + english + physics) / 3


def classify(avg):
    if avg >= 8:
        return "Gioi"

    elif avg >= 6.5:
        return "Kha"

    elif avg >= 5:
        return "Trung Binh"

    else:
        return "Yeu"


def highest_score(math, english, physics):
    return max(math, english, physics)


def lowest_score(math, english, physics):
    return min(math, english, physics)