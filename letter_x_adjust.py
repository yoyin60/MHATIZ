from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Create a blank white image
img_size = (200, 200)
img = Image.new("RGB", img_size, "white")
draw = ImageDraw.Draw(img)

# Choose a font; fallback to default if not available
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 120)
except IOError:
    font = ImageFont.load_default()

# Draw the letter X in the center
text = "X"
text_width, text_height = draw.textsize(text, font=font)
position = ((img_size[0] - text_width) // 2, (img_size[1] - text_height) // 2)
draw.text(position, text, fill="black", font=font)

# Save the original image
img.save("letter_x_original.png")

# Apply a small blur filter
blurred = img.filter(ImageFilter.GaussianBlur(radius=2))
blurred.save("letter_x_blurred.png")

# Apply a sharpen filter
sharpened = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150,
    threshold=3))
sharpened.save("letter_x_sharpened.png")

print("Images saved: letter_x_original.png, letter_x_blurred.png, letter_x_sharpened.png")
