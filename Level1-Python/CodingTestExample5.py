#문제 설명

#숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있습니다. 기사들은 무기점에서 무기를 구매하려고 합니다.
#각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다.
#단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고,
#제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.
#예를 들어, 15번으로 지정된 기사단원은 15의 약수가 1, 3, 5, 15로 4개 이므로, 공격력이 4인 무기를 구매합니다.
#만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 제한수치를 초과한 기사가 사용할 무기의 공격력이 2라면,
#15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다.
#그래서 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게를 미리 계산하려 합니다.
#기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는
#정수 limit와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때,
#무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.

# 제한사항
#1 ≤ number ≤ 100,000
#2 ≤ limit ≤ 100
#1 ≤ power ≤ limit

#입출력 예
#number	limit	power	result

#5	3	2	10
#10	3	2	21

#시간초과로 인한 비효율 코드
def solution(number, limit, power):
    if not 1 <= number <= 100000 or not 2 <= limit <= 100 or not 1 <= power <= limit:
        return "False"

    result = 0
    for i in range(1, (number + 1)):
        num = 0
        for k in range(1, i + 1):
            if i % k == 0:
                num += 1
        if num <= limit:
            result += num
        else:
            result += power

    return result




# 개선된 코드
def solution(number, limit, power):
    if not 1 <= number <= 100000 or not 2 <= limit <= 100 or not 1 <= power <= limit:
        raise ValueError("잘못된 입력 값")

    result = 0
    for i in range(1, number + 1):
        num_divisors = 0
        for k in range(1, int(i**0.5) + 1):
            if i % k == 0:
                num_divisors += 1
                if i // k != k:
                    num_divisors += 1
        if num_divisors <= limit:
            weapon_power = num_divisors
        else:
            weapon_power = power
        result += weapon_power

    return result
#입출력 예 설명

#입출력 예 #1

#1부터 5까지의 약수의 개수는 순서대로 [1, 2, 2, 3, 2]개입니다.
#모두 공격력 제한 수치인 3을 넘지 않기 때문에 필요한 철의 무게는 해당 수들의 합인 10이 됩니다. 따라서 10을 return 합니다.

#입출력 예 #2

#1부터 10까지의 약수의 개수는 순서대로 [1, 2, 2, 3, 2, 4, 2, 4, 3, 4]개입니다.
# 공격력의 제한수치가 3이기 때문에, 6, 8, 10번 기사는 공격력이 2인 무기를 구매합니다.
# 따라서 해당 수들의 합인 21을 return 합니다.