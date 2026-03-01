if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    
    unique_scores = sorted(list(set([s[1] for s in students])))
    
  
    second_lowest_val = unique_scores[1]
    
  
    low_scorers = [s[0] for s in students if s[1] == second_lowest_val]
    low_scorers.sort()
    

    for name in low_scorers:
        print(name)
