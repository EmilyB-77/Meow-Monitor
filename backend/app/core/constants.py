"""Application constants."""

# Mood tracking values
MOOD_CHOICES = ["happy", "content", "neutral", "anxious", "grumpy", "playful", "tired"]

# Health record types
HEALTH_RECORD_TYPES = [
    "vaccination",
    "checkup",
    "medication",
    "surgery",
    "dental",
    "allergy",
    "weight_check",
    "behavioral",
]

# Feeding portion sizes (grams)
PORTION_SIZES = {
    "small": 30,
    "medium": 50,
    "large": 75,
}

# Food types
FOOD_TYPES = ["wet", "dry", "mixed"]

# Default pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# File upload
MAX_FILENAME_LENGTH = 255
UPLOAD_DIRECTORY = "uploads"