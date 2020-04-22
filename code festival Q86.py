'''

Q. 각 초밥 점수를 매기고 낮은 점수의 순서로 초밥을 먹을 때, n번째 위치에 놓여진 초밥은 몇 번 지나가고 먹을수 있는지 출력.

A. 문제풀이과정
    1. 초밥의 점수는 순차적으로 증가하지 않음.
        > 초밥 목록이 [1,1,3,2,5]와 같다면, 4점의 초밥이 없으므로 sort로 별도의 초밥 점수 목록 생성.
    2. 같은 등급의 초밥이라도 index가 다르면 다른 초밥.
        > 단순히 n번째 위치의 초밥 점수와 초밥 목록의 값을 비교할 수 없음. index 값을 비교하는 조건문이 필요.

'''

def favorite_sushi(sushi_list, n):
    index = n-1
    count = 0
    grade_list = sorted(sushi_list)

    while True :
        sushi = sushi_list.pop(0)
        if grade_list[0] == sushi :
            if index == 0:
                break
            index -= 1
            grade_list.pop(0)
        else:
            sushi_list.append(sushi)
            index = len(sushi_list) - 1 if index == 0 else index-1
        count+=1

    return count

example=[5,2,3,1,2,5]
dish=1
result='회전초밥의 점수는 {}이며, 그중 {}번째 초밥을 먹기 위해서 {}번의 접시를 지나가야한다.'
print(result.format(example[:], dish, favorite_sushi(example, dish)))
