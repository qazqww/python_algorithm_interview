def reorderLogFiles(self, logs: list[str]) -> list[str]:
    let_list, dig_list = [], []
    for log in logs:
        if log.split(' ')[1].isdigit():
            dig_list.append(log)
        else:
            let_list.append(log)
            
    # 정렬을 어떤 식으로 할지는 떠올랐으나, 코드로 구현하기엔 지저분한 방법밖에 떠오르지 않았다
    # split()의 활용과 람다식에 대한 지식이 부족했음
    let_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return let_list + dig_list