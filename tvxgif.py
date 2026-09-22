from PIL import Image, ImageDraw, ImageFont
import math

width, height = 600, 400
frames_count = 30
duration_per_frame = 70

try:
    font = ImageFont.truetype("arial.ttf", 80)
except IOError:
    font = ImageFont.load_default()

frames = []
text = "tvx"

for i in range(frames_count):
    img = Image.new("RGB", (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    progress = i / frames_count
    
    red = int(212 + 43 * math.sin(progress * 2 * math.pi))
    green = int(175 + 50 * math.sin(progress * 2 * math.pi))
    blue = int(55 + 50 * math.cos(progress * 2 * math.pi))
    text_color = (red, green, blue)
    
    shadow_offset = int(4 * math.sin(progress * 2 * math.pi))
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    draw.text((x + 2, y + 2 + shadow_offset), text, fill=(30, 30, 30), font=font)
    draw.text((x, y + shadow_offset), text, fill=text_color, font=font)
    
    frames.append(img)

output_filename = "tvx_animation.gif"
frames[0].save(
    output_filename,
    save_all=True,
    append_images=frames[1:],
    optimize=False,
    duration=duration_per_frame,
    loop=0
)

print(f"تم الحفظ: {output_filename}")
