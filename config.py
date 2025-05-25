"""Configuration for the static page generator."""

# Sketchbooks to generate (name, title)
SKETCHBOOKS = [
    ("sb1", "Sketchbook 1"),
    ("sb2", "Sketchbook 2"),
    ("sb3", "Sketchbook 3"),
    ("sb4", "Sketchbook 4"),
    ("sb5", "Sketchbook 5")
]

# File extensions to include
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']

# Number of images to load eagerly (rest will be lazy-loaded)
EAGER_LOAD_COUNT = 4