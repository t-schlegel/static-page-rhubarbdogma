#!/usr/bin/env python3
"""
Generate static HTML pages for archive sketchbooks and sketchdump.
This replaces the dynamic FastHTML generation with static files.
"""

import os
import glob
from pathlib import Path

def generate_sketchbook_page(sketchbook_name, title, static_dir, archive_dir):
    """Generate an individual sketchbook page with all images."""
    
    # Get all JPG files in the sketchbook directory
    image_dir = os.path.join(archive_dir, sketchbook_name)
    if not os.path.exists(image_dir):
        print(f"Warning: Directory {image_dir} does not exist")
        return
    
    jpg_files = sorted([f for f in os.listdir(image_dir) if f.lower().endswith('.jpg')])
    
    # Generate image HTML
    images_html = ""
    for i, img_file in enumerate(jpg_files):
        loading = 'eager' if i < 4 else 'lazy'
        images_html += f'''        <img src="/archive/{sketchbook_name}/{img_file}" loading="{loading}" class="w-full h-auto object-cover rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 transition-all ease-in-out w-full">\n'''
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>rhubarb dogma</title>
    <link rel="stylesheet" href="../style.css">
    <link rel="stylesheet" href="../css/scrollbar.css">
    <link rel="stylesheet" href="../css/modal.css">
</head>
<body class="bg-gray-100 p-4 md:p-8">
    <header class="absolute top-0 left-0 m-4">
        <a href="/" class="font-times text-xl hover:underline">rhubarb dogma</a>
    </header>
    
    <span class="font-times block mt-24 mb-8 text-3xl center-text flex items-center justify-center">{title}</span>
    
    <div class="gallery max-w-6xl mx-auto">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
{images_html}        </div>
    </div>

    <!-- Modal for image viewing -->
    <div id="imageModal" class="modal hidden">
        <div class="modal-content">
            <button id="prev" class="nav-button">
                <img src="../svg/prev.svg" width="100" height="100" class="nav-button transition brightness-100 hover:brightness-100 hover:scale-110 transform transition-transform active:brightness-100">
            </button>
            <img id="modalImage" src="" alt="Modal Image" class="modal-img">
            <button id="next" class="nav-button">
                <img src="../svg/next.svg" width="100" height="100" class="nav-button transition brightness-100 hover:brightness-100 hover:scale-110 transform transition-transform active:brightness-100">
            </button>
        </div>
    </div>

    <script src="../js/modal.js"></script>
</body>
</html>"""
    
    # Write the HTML file
    archive_static_dir = os.path.join(static_dir, "archive")
    os.makedirs(archive_static_dir, exist_ok=True)
    
    output_file = os.path.join(archive_static_dir, f"{sketchbook_name}.html")
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"Generated {output_file}")

def generate_sketchdump_page(static_dir, sketchdump_dir):
    """Generate the sketchdump page with all sketch images."""
    
    if not os.path.exists(sketchdump_dir):
        print(f"Warning: Directory {sketchdump_dir} does not exist")
        return
    
    # Get all JPG files in the sketchdump directory
    jpg_files = sorted([f for f in os.listdir(sketchdump_dir) if f.lower().endswith('.jpg')])
    
    # Split images into two columns (even/odd)
    even_images = []
    odd_images = []
    
    for i, img_file in enumerate(jpg_files):
        loading = 'eager' if i < 4 else 'lazy'
        img_html = f'            <img src="/sketchdump/{img_file}" loading="{loading}" class="w-full h-auto object-cover rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 transition-all ease-in-out w-full">'
        
        if i % 2 == 0:
            even_images.append(img_html)
        else:
            odd_images.append(img_html)
    
    even_column = "\\n".join(even_images)
    odd_column = "\\n".join(odd_images)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>rhubarb dogma</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="css/scrollbar.css">
    <link rel="stylesheet" href="css/modal.css">
</head>
<body class="bg-gray-100 p-4 md:p-8">
    <header class="absolute top-0 left-0 m-4">
        <a href="/" class="font-times text-xl hover:underline">rhubarb dogma</a>
    </header>
    
    <div class="py-13"></div>
    <div class="py-16"></div>
    
    <span class="font-times block text-4xl md:text-9xl mb-8 center-text flex items-center justify-center">Sketch Dump</span>
    
    <div class="gallery max-w-6xl mx-auto">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div class="flex flex-col gap-4">
{even_column}
            </div>
            <div class="flex flex-col gap-4">
{odd_column}
            </div>
        </div>
    </div>

    <!-- Modal for image viewing -->
    <div id="imageModal" class="modal hidden">
        <div class="modal-content">
            <button id="prev" class="nav-button">
                <img src="/svg/prev.svg" width="100" height="100" class="nav-button transition brightness-100 hover:brightness-100 hover:scale-110 transform transition-transform active:brightness-100">
            </button>
            <img id="modalImage" src="" alt="Modal Image" class="modal-img">
            <button id="next" class="nav-button">
                <img src="/svg/next.svg" width="100" height="100" class="nav-button transition brightness-100 hover:brightness-100 hover:scale-110 transform transition-transform active:brightness-100">
            </button>
        </div>
    </div>

    <script src="js/modal.js"></script>
</body>
</html>"""
    
    # Write the HTML file
    output_file = os.path.join(static_dir, "sketchdump.html")
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"Generated {output_file}")

def main():
    # Define paths
    project_root = "/home/nox/src/static-page-rhubarbdogma"
    static_dir = os.path.join(project_root, "static")
    archive_base_dir = os.path.join(static_dir, "archive")
    sketchdump_dir = os.path.join(static_dir, "sketchdump")
    
    # Generate sketchbook pages
    sketchbooks = [
        ("sb1", "Sketchbook 1"),
        ("sb2", "Sketchbook 2"), 
        ("sb3", "Sketchbook 3"),
        ("sb4", "Sketchbook 4"),
        ("sb5", "Sketchbook 5")
    ]
    
    for sketchbook_name, title in sketchbooks:
        generate_sketchbook_page(sketchbook_name, title, static_dir, archive_base_dir)
    
    # Generate sketchdump page
    generate_sketchdump_page(static_dir, sketchdump_dir)
    
    print("All pages generated successfully!")

if __name__ == "__main__":
    main()