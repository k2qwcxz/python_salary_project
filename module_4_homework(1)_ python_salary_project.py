def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        name, salary_str = line.rsplit(',', 1)
                        salary = int(salary_str)
                        total += salary
                        count += 1
                    except (ValueError, IndexError):
                        continue
        
        average = total / count if count > 0 else 0
        return total, average
        
    except FileNotFoundError:
        return 0, 0
    except Exception:
        return 0, 0
    

if __name__=="__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітньої плати: {total}, Середня заробітна плата: {average}") 