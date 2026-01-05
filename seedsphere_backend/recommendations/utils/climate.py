def detect_climate(latitude):
    if -23.5 <= latitude <= 23.5:
        return "Tropical"
    elif 23.5 < latitude <= 40:
        return "Subtropical"
    else:
        return "Temperate"
