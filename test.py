from PIL import Image, ImageDraw, ImageFont

# Load the original image
image_path = "image.png"
image = Image.open(image_path)

# Create a draw object
draw = ImageDraw.Draw(image)

# Define new values with Amharic names and positions to replace
edits = [
    {"text": "Kaleab", "position": (70, 390)},  # Replacing 'Mr Junayed'
    {"text": "Addis Ababa", "position": (420, 390)},    # Replacing 'Mirpur 10'
    {"text": "Abyssinia bank", "position": (680, 810)},  # Replacing 'DBBL'
]


font = ImageFont.load_default()

# Apply the edits
for edit in edits:
    draw.text(edit["position"], edit["text"], fill="black", font=font)

# Save the edited image
edited_image_path = "edited_image.png"
image.save(edited_image_path)

edited_image_path
