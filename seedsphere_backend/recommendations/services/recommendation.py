from recommendations.static_data import PLANTS


def get_recommendations(preferences):
    climate = preferences.get("climate")
    soil = preferences.get("soil")
    category = preferences.get("category")

    results = []

    for plant in PLANTS:
        if climate and plant["climate"] != climate:
            continue
        if soil and soil != "All" and plant["soil"] != soil:
            continue
        if category and category != "All" and plant["category"] != category:
            continue

        results.append(plant)

    return results
