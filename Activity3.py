#Amanda Odvody
#ISQA 3900
# 2/9/23
#This code's purpose is to take the user's input and use that to figure out
#a letter grade
def display_title():
    print("Welcome to the Grade Calculator!")


def get_totalPoints():
    totalPointsInput = input("Enter total score (0-1000): ")
    if totalPointsInput.isnumeric() == True:
        totalPoints = int(totalPointsInput)
        if totalPoints < 0 or totalPoints > 1000:
            totalPoints = int(input("Error. Reenter value between 0-1000"))
            return totalPoints
        else:
            return totalPoints
    if totalPointsInput.isnumeric() == False:
        totalPoints = int(input("Enter a numeric value (0-1000): "))
        return totalPoints


def get_letterGrade(averageEarned):
    if 100 >= averageEarned >= 92:
        return "A"
    if 91.99 >= averageEarned >= 88:
        return "B+"
    if 87.99 >= averageEarned >= 82:
        return "B"
    if 81.99 >= averageEarned >= 78:
        return "C+"
    if 77.99 >= averageEarned >= 70:
        return "C"
    if 69.99 >= averageEarned >= 60:
        return "D"
    else:
        return "F"


def main():
    display_title()
    print()
    ans = 'y'
    allPoints = 0
    while ans.lower() == 'y':
        allPoints += get_totalPoints()
        averageEarned = float(allPoints / 1000 * 100)
        get_letterGrade(averageEarned)
        print(f'You earned a(n) {get_letterGrade(averageEarned)}')
        ans = input("Do you wish to continue? y/n ")
    print("Goodbye")


if __name__ == '__main__':
    main()
