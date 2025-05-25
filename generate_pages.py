#!/usr/bin/env python3
"""
Generate static HTML pages for archive sketchbooks and sketchdump.
This replaces the dynamic FastHTML generation with static files.
"""

import os
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import config


class PageGenerator:
    """Handles generation of static HTML pages using Jinja2 templates."""
    
    def __init__(self):
        # Get script directory and set up paths
        self.script_dir = Path(__file__).parent.absolute()
        self.static_dir = self.script_dir / "static"
        self.templates_dir = self.script_dir / "templates"
        self.archive_dir = self.static_dir / "archive"
        self.sketchdump_dir = self.static_dir / "sketchdump"
        
        # Set up Jinja2 environment
        try:
            self.env = Environment(loader=FileSystemLoader(self.templates_dir))
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Jinja2 environment: {e}")
    
    def _validate_directories(self):
        """Validate that required directories exist."""
        if not self.static_dir.exists():
            raise FileNotFoundError(f"Static directory not found: {self.static_dir}")
        if not self.templates_dir.exists():
            raise FileNotFoundError(f"Templates directory not found: {self.templates_dir}")
    
    def _get_image_files(self, directory):
        """Get sorted list of image files from a directory."""
        if not directory.exists():
            return []
        
        image_files = []
        for ext in config.IMAGE_EXTENSIONS:
            image_files.extend(directory.glob(f"*{ext}"))
            image_files.extend(directory.glob(f"*{ext.upper()}"))
        
        return sorted([f.name for f in image_files])
    
    def _create_image_data(self, image_files, base_path):
        """Create image data list with loading attributes."""
        images = []
        for i, img_file in enumerate(image_files):
            loading = 'eager' if i < config.EAGER_LOAD_COUNT else 'lazy'
            images.append({
                'src': f"{base_path}/{img_file}",
                'loading': loading
            })
        return images
    
    def generate_sketchbook_page(self, sketchbook_name, title):
        """Generate an individual sketchbook page with all images."""
        try:
            # Get image files
            image_dir = self.archive_dir / sketchbook_name
            if not image_dir.exists():
                print(f"Warning: Directory {image_dir} does not exist, skipping {sketchbook_name}")
                return False
            
            image_files = self._get_image_files(image_dir)
            if not image_files:
                print(f"Warning: No images found in {image_dir}, skipping {sketchbook_name}")
                return False
            
            # Create image data
            images = self._create_image_data(image_files, f"/archive/{sketchbook_name}")
            
            # Render template
            template = self.env.get_template('sketchbook.html')
            html_content = template.render(
                title=title,
                images=images,
                css_path="../",
                svg_path="../svg/",
                js_path="../js/"
            )
            
            # Write output file
            output_dir = self.static_dir / "archive"
            output_dir.mkdir(exist_ok=True)
            output_file = output_dir / f"{sketchbook_name}.html"
            
            output_file.write_text(html_content, encoding='utf-8')
            print(f"Generated {output_file}")
            return True
            
        except Exception as e:
            print(f"Error generating sketchbook page for {sketchbook_name}: {e}")
            return False
    
    def generate_sketchdump_page(self):
        """Generate the sketchdump page with all sketch images."""
        try:
            if not self.sketchdump_dir.exists():
                print(f"Warning: Directory {self.sketchdump_dir} does not exist")
                return False
            
            # Get image files
            image_files = self._get_image_files(self.sketchdump_dir)
            if not image_files:
                print(f"Warning: No images found in {self.sketchdump_dir}")
                return False
            
            # Split images into two columns (even/odd)
            all_images = self._create_image_data(image_files, "/sketchdump")
            even_images = [img for i, img in enumerate(all_images) if i % 2 == 0]
            odd_images = [img for i, img in enumerate(all_images) if i % 2 == 1]
            
            # Render template
            template = self.env.get_template('sketchdump.html')
            html_content = template.render(
                even_images=even_images,
                odd_images=odd_images,
                css_path="",
                svg_path="/svg/",
                js_path="js/"
            )
            
            # Write output file
            output_file = self.static_dir / "sketchdump.html"
            output_file.write_text(html_content, encoding='utf-8')
            print(f"Generated {output_file}")
            return True
            
        except Exception as e:
            print(f"Error generating sketchdump page: {e}")
            return False
    
    def generate_all(self):
        """Generate all pages."""
        try:
            self._validate_directories()
            
            success_count = 0
            total_count = 0
            
            # Generate sketchbook pages
            for sketchbook_name, title in config.SKETCHBOOKS:
                total_count += 1
                if self.generate_sketchbook_page(sketchbook_name, title):
                    success_count += 1
            
            # Generate sketchdump page
            total_count += 1
            if self.generate_sketchdump_page():
                success_count += 1
            
            if success_count == total_count:
                print("All pages generated successfully!")
                return True
            else:
                print(f"Generated {success_count}/{total_count} pages successfully")
                return False
                
        except Exception as e:
            print(f"Error during page generation: {e}")
            return False


def main():
    """Main entry point."""
    try:
        generator = PageGenerator()
        success = generator.generate_all()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()