from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from recommendations.services.recommendation import get_recommendations
from recommendations.utils.climate import detect_climate


@api_view(["POST"])
def recommend_plants(request):
    """
    API to recommend plants based on real user location and preferences
    """

    latitude = request.data.get("latitude")
    longitude = request.data.get("longitude")  # optional (future use)

    # --- Validate latitude ---
    if latitude is None:
        return Response(
            {"error": "Latitude is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        latitude = float(latitude)
    except ValueError:
        return Response(
            {"error": "Invalid latitude value"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # --- Detect climate from latitude ---
    climate = detect_climate(latitude)

    # --- Build preference dictionary ---
    preferences = {
        "soil": request.data.get("soil", "All"),
        "sunlight": request.data.get("sunlight", "All"),
        "category": request.data.get("category", "All"),
        "climate": climate
    }

    # --- Get plant recommendations ---
    plants = get_recommendations(preferences)

    # --- Final response ---
    return Response(
        {
            "climate": climate,
            "recommended_plants": plants,
            "count": len(plants)
        },
        status=status.HTTP_200_OK
    )

