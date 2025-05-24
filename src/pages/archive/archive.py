from fasthtml.common import *

from utils.core import prefetch_img_tags


@flexicache()
def archive():
  return (
    Head(
      Title("rhubarb dogma"),
      Meta(name='viewport', charset='UTF-8', content='width=device-width, initial-scale=1.0'),
      StyleX("css/scrollbar.css"),
      *prefetch_img_tags("/archive/sb5"),
      *prefetch_img_tags("/archive/sb4"),
      *prefetch_img_tags("/archive/sb3"),
      *prefetch_img_tags("/archive/sb2"),
      *prefetch_img_tags("/archive/sb1"),
    ),
    Body(
      Header(
        A('rhubarb dogma', cls='font-times text-xl hover:underline', href="/"),
        cls='absolute top-0 left-0 m-4',
      ),
      Nav(
        cls='absolute top-0 right-0 m-4',
      ),
      Div(
        Div(
          Div(cls="py-16"),
          Span('Archive', cls='font-times block text-7xl md:text-9xl mb-8 text-center'),
          Div(
            sketchbook("/archive/sb5.jpg", "230px", "371px", "Jun 2024 - Ongoing", "Sketchbook 5", "/archive/sb5"),
            sketchbook("/archive/sb4.jpg", "230px", "350px", "Apr 2024 - Ongoing", "sketchbook 4", "/archive/sb4"),
            sketchbook("/archive/sb3.jpg", "230px", "320px", "Oct 2023 - Jun 2024", "Sketchbook 3", "/archive/sb3"),
            # cls='flex flex-wrap justify-center gap-4 sm:flex sm:space-x-8 sm:items-end sm:flex-nowrap',
            cls='flex flex-wrap justify-center gap-4 items-end md:space-x-8',
          ),
          cls='sm:flex sm: flex-col md:flex md:flex-col items-center mt-8 font-times',
        ),
        Div(
          Div(
            sketchbook("/archive/sb2.jpg", "230px", "355px", "Jan 2024 - Apr 2024", "Sketchbook 2", "/archive/sb2"),
            sketchbook("/archive/sb1.jpg", "230px", "355px", "Aug 2023 - Dec 2023", "Sketchbook 1", "/archive/sb1"),
            # cls='flex flex-wrap justify-center gap-4 sm:flex sm:space-x-8 sm:items-end sm:flex-nowrap',
            cls='flex flex-wrap justify-center gap-4 items-end md:space-x-8',
          ),
          Div("", cls="py-8"),
          cls='items-center mt-8 font-times',
        ),
        cls='justify-center',
      ),
    ),
  )


@flexicache()
def sketchbook(imgpath: str, width: str, height: str, date: str, name: str, url: str):
  return (
    A(
      card(imgpath, width, height),
      Div(cls='py-2'),
    	Div(name, cls='text-center text-sm py-2'),
    	Div(date, cls='text-center text-xs text-gray-500'),
    	cls='flex flex-col items-center',
      href=url,
    )
  )

# Design credit: https://codepen.io/markmiro/pen/wbqMPa
def card(img_url, width="235px", height="335px"):
   """This is a standalone isolated Python component.
   Behavior and styling is scoped to the component.
   """
   def card_3d(text, background, amt, left_align):
       scr = ScriptX('js/card3d.js', amt=amt)
       align = 'left' if left_align else 'right'
       sty = StyleX('css/card3d.css', background=f'url({img_url})', align=align, width=width, height=height)
       return Div(text, Div(), sty, scr)
   cardcss = StyleX("css/card.css")
   return Div(card_3d("", img_url, amt=1.5, left_align=True), style=cardcss)
