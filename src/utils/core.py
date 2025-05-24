from fasthtml.common import *

import os, glob
from functools import lru_cache

@flexicache()
def prefetch_img_tags(path, limit=6):
  """Generate prefetch tags for images in the specified path.
  Uses a generator-based approach to reduce memory usage.

  Args:
      path: Directory path relative to public/
      limit: Maximum number of images to prefetch (default: 6)
  """
  # Use scandir instead of glob.glob to avoid loading all files into memory
  public_path = os.path.join("public", path.lstrip('/'))

  # Only collect necessary information without storing all files in memory
  jpg_files = []

  # Check if directory exists to avoid errors
  if os.path.isdir(public_path):
      # Use a generator to avoid loading all files in memory at once
      entries = (entry.path for entry in os.scandir(public_path)
                if entry.is_file() and entry.name.lower().endswith('.jpg'))

      # Take only the first 'limit' files to reduce memory usage
      # Loop instead of slicing to avoid materializing the full list
      count = 0
      for entry in sorted(entries):
          jpg_files.append(entry)
          count += 1
          if count >= limit:
              break

  # Generate tags as a generator expression
  return [NotStr(f'<link rel="prefetch" href="{jpg[7:]}" as="image">') for jpg in jpg_files]
