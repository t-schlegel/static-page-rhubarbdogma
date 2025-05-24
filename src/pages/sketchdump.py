from fasthtml.common import *

from components.gallery import generate_sd_sketches, modal

base_path = "/sketchdump"
physical_path = "public/sketchdump"

@flexicache()
def sketchdump():
  return (
    Head(
      Title("rhubarb dogma"),
      Meta(name='viewport', charset='UTF-8', content='width=device-width, initial-scale=1.0'),
      StyleX("css/scrollbar.css"),
      StyleX("css/modal.css"),
    ),
  Body(
    Header(
        A('rhubarb dogma', cls='font-times text-xl hover:underline', href="/",
        ),
        cls='absolute top-0 left-0 m-4',
    ),
    Div(cls="py-13"),
    Div(cls="py-16"),
    Span('Sketch Dump', cls='font-times block text-4xl md:text-9xl mb-8 center-text flex items-center justify-center'),
    Div(
      Div(
        # Use generate_sd_sketches to create two independent columns
        # This allows images to have different heights without forcing vertical alignment
        *generate_sd_sketches(base_path, physical_path, limit=100),
        cls='grid grid-cols-1 sm:grid-cols-2 gap-4',
      ),
      cls='gallery max-w-6xl mx-auto',
    ),
    modal(),
    cls='bg-gray-100 p-4 md:p-8',
  ),
)
