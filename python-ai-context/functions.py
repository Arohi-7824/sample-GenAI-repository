def normalize_date(data,method='min-max'):
    '''Normalize data for ML models'''
    if method == 'min-max':
        min_val = min(data)
        max_val = max(data)
        return [(x - min_val) / (max_val - min_val) for x in data]
    elif method == 'z-score':
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        return [(x - mean) / std_dev for x in data]

raw_data=[10, 20, 30, 40, 50]

normalize=normalize_date(raw_data)
print("Normalized data:", normalize)