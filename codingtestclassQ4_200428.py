동물 = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']

def solution(동물, 자리):
    의자 = [] * 자리
    answer = 0
    for i in 동물:
        if len(의자) < 3:
            if i in 의자:
                의자.append(의자.pop(0))
                answer += 1
            else:
                의자.append(i)
                answer += 60
        else:
            if i in 의자:
                의자.append(의자.pop(0))
                answer += 1
            else:
                의자.pop(0)
                의자.append(i)
                answer += 60

    return answer

    
solution(동물, 3)
