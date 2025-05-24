from fasthtml.common import *

from components.gallery import generate_sketches, modal

base_path = "/archive/sb2"
physical_path = "public/archive/sb2"

@flexicache()
def sb2():
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
    Span('Sketchbook 2', cls='font-times block mt-24 mb-8 text-3xl center-text flex items-center justify-center '),
    Div(
      Div(
        *generate_sketches(base_path, physical_path, limit=100),
        cls='grid grid-cols-1 sm:grid-cols-2 gap-4',
      ),
      cls='gallery max-w-6xl mx-auto',
    ),
    modal(),
    cls='bg-gray-100 p-4 md:p-8',
  ),
)
