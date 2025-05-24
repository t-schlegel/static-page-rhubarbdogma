import os

from fasthtml.common import *

def sketch(url: str, loading="lazy"):
  return Img(src=url, loading=loading, cls='w-full h-auto object-cover rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 transition-all ease-in-out w-full')

def generate_sketches(base_path="/archive/sb1", physical_path="public/archive/sb1", limit=None):
    #IMPORTANT: DON'T USE - USE generate_sketches() below
    # Generate sketch elements for images using a generator to save memory
    # Use scandir instead of listdir for better performance
    # Process files in a streaming fashion
    count = 0
    eager_count = 4

    # Get jpg files using a generator expression instead of list comprehension
    # This prevents loading all filenames into memory at once
    image_files = (f.name for f in os.scandir(physical_path)
                   if f.is_file() and f.name.lower().endswith('.jpg'))

    # Sort the file names - needed for consistent ordering
    # Use sorted with a generator to reduce peak memory
    sorted_files = sorted(image_files)

    # First few images load eagerly, others lazy load
    for i, img_file in enumerate(sorted_files):
        if limit is not None and count >= limit:
            break

        img_path = f"{base_path}/{img_file}"
        loading = 'eager' if i < eager_count else 'lazy'
        yield sketch(img_path, loading=loading)
        count += 1

def generate_sd_sketches(base_path, physical_path, limit=None):
    """
    Split sketches into two columns (even/odd) without loading everything twice.
    This is a memory-efficient replacement for the double enumeration approach.

    Args:
        base_path: Web path for images
        physical_path: Filesystem path to load images from
        limit: Maximum total number of images to load

    Returns:
        Two column divs with the sketches distributed evenly/odd between them
    """
    even_sketches = []
    odd_sketches = []

    for i, sketch_elem in enumerate(generate_sketches(base_path, physical_path, limit)):
        if i % 2 == 0: even_sketches.append(sketch_elem)
        else: odd_sketches.append(sketch_elem)

    # Return two divs with the properly split sketches
    return [
        Div(*even_sketches, cls='flex flex-col gap-4'),
        Div(*odd_sketches, cls='flex flex-col gap-4')
    ]

def modal():
  return (
    Div(
     Div(
       Button(
         Img(src='/svg/prev.svg', width='100', height='100',
             cls='nav-button transition brightness-100 hover:brightness-100 hover:scale-110 transform transition-transform active:brightness-100',
         ),
         id='prev', cls='nav-button',
       ),
         Img(id='modalImage', src='', alt='Modal Image', cls='modal-img'),
         Button(
             Img(src='/svg/next.svg', width='100', height='100',
              cls='nav-button transition  brightness-100 hover:brightness-100 hover:scale-110 transform transition-transform  active:brightness-100'),
             id='next',
             cls='nav-button',
         ),
         cls='modal-content',
     ),
     ScriptX("js/modal.js"),
     id='imageModal',
     cls='modal hidden',
    )
  )
