from student import input_student

from score import calculate_average
from score import classify
from score import highest_score
from score import lowest_score

from report import print_report


def main():

    name, math, english, physics = input_student()

    avg = calculate_average(math, english, physics)

    rank = classify(avg)

    highest = highest_score(math, english, physics)

    lowest = lowest_score(math, english, physics)

    print_report(
        name,
        avg,
        rank,
        highest,
        lowest
    )


if __name__ == "__main__":
    main()