def process_music_data(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    
    header = lines[0].strip().split(";")
    data = [line.strip().split(";") for line in lines[1:]]
    
    compositores = sorted(set(row[4] for row in data if len(row) > 4))

    periodos = {}
    obras_periodo = {}
    for row in data:
        if len(row) > 3:
            periodo = row[3]
            titulo = row[0]
            
            periodos[periodo] = periodos.get(periodo, 0) + 1
