from fasthtml.common import *


@flexicache()
def sepine_forest():
  return (
    Head(
      Meta(name='viewport', charset='UTF-8', content='width=device-width, initial-scale=1.0'),
      Title("Sepine - Fungi Forest"),
    ),
    Body(
      Header(
        A('rhubarb dogma', cls='font-times text-xl hover:underline', href="/"),
        cls='absolute top-0 left-0 m-4',
      ),
      Div(
        Img(src='/ytc/sepine/sepine-forest.jpg', usemap='#image-map', cls='scale-[125%]'),
      ),
      cls="flex justify-center items-center min-h-screen",
    ),
  )