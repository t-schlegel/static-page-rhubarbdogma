from fasthtml.common import *

from utils.core import prefetch_img_tags


@flexicache()
def index():
  return (
    Title("rhubarb dogma"),
    Head(
      *prefetch_img_tags("archive"),
      *prefetch_img_tags("sketchdump"),
    ),
      Body(
        Header(
          A('rhubarb dogma', cls='font-times text-xl hover:underline absolute top-0 left-0 m-4 z-10',
          href="/"),
          Nav(
            cls='absolute top-0 right-0 m-4 z-10',
          ),
        ),
        Div(
        Div(
          # Grid layout for medium screens and above
          Div(
            A(
              Div(
                Img(src='/svg/archive-1.svg', cls='w-full h-full group-hover:hide transition-all group-hover:opacity-0 transform'),
                Img(src='/svg/archive-2.svg', cls='w-full h-full absolute top-0 left-0 opacity-0 transition-all group-hover:opacity-100 transform group-hover:animate-spin'),
                cls='group flex flex-col items-center relative w-full h-full',
              ),
              cls='id="archive" col-start-14 row-start-18 row-span-28 col-span-28 relative cursor-pointer -rotate-[13deg]',
              href="/archive",
            ),

            A(
              Div(
                Img(src='/svg/ytc-1.svg', cls='absolute w-full h-full group-hover:hide group-hover:opacity-0 transform rotate-1 transition-all ease-in-out'),
                Img(src='/svg/ytc-2.svg', cls='absolute w-full h-full top-0 left-0 opacity-0 group-hover:opacity-100 transform transition-all ease-in-out rotate-7'),
                cls='group col-span-13 row-span-13 relative items-center relative w-full h-full',
              ),
              href="/ytc/sepine",
              cls='id="ytc" col-start-70 row-start-25 col-span-18 row-span-18 relative item-center w-full h-full object-cover',
            ),

            A(
              Div(
                Img(src='/svg/datura-1.svg', cls='items-center justify-center group-hover:hide group-hover:opacity-0 transform transition-all ease-in-out'),
                Img(src='/svg/datura-2.svg', cls='absolute items-center justify-center left-0 opacity-0 transition-all group-hover:opacity-100 transform scale-100 ease-in-out'),
                cls='group col-span-20 row-span-20 relative flex flex-col items-center relative',
              ),
              href='#',
              id="datura",
              cls='col-start-46 row-start-20 col-span-18 row-span-18 w-full h-full object-cover relative',
            ),

            A(
              Div(
                Img(src='/svg/sketch-dump-1.svg', cls='w-full h-full group-hover:hide group-hover:opacity-0 transform rotate-0 ease-in-out transition-all ease-in-out'),
                Img(src='/svg/sketch-dump-2.svg', cls='absolute top-0 left-0 w-full h-full opacity-0 group-hover:opacity-100 transform rotate-2 ease-in-out transition-all ease-in-out'),
                cls='group col-span-16 row-span-16 relative items-center relative',
              ),
              href='/sketchdump',
              cls='id="sketch-dump" col-start-20 row-start-70 col-span-16 row-span-16 w-full h-full object-cover relative',
            ),
            A(
              Div(
                Img(src='/svg/grotto-goblins-1.svg', cls='w-full h-full group-hover:hide group-hover:opacity-0 transform rotate-3 ease-in-out transition-all ease-in-out'),
                Img(src='/svg/grotto-goblins-2.svg', cls='w-full h-full absolute top-0 left-0 opacity-0 duration-100 transition-all group-hover:opacity-100 transform rotate-7 ease-in-out'),
                cls='group relative items-center',
              ),
              href='#',
              cls='id="sketch-dump" col-start-75 row-start-65 col-span-12 row-span-12 w-full h-full object-cover relative',
            ),
            cls='hidden md:grid md:grid-cols-100 md:grid-rows-100 gap-0 h-[95vh] w-[95vw] relative',
            id="desktop-grid",
          ),

          # Single column layout for mobile devices
          Div(
            A(
              Div(
                Img(src='/svg/archive-1.svg', cls='w-full h-full group-hover:hide transition-all group-hover:opacity-0 transform'),
                Img(src='/svg/archive-2.svg', cls='w-full h-full absolute top-0 left-0 opacity-0 transition-all group-hover:opacity-100 transform group-hover:animate-spin'),
                cls='group flex flex-col items-center relative w-full h-full',
              ),
              cls='block w-4/5 mx-auto my-8 relative cursor-pointer',
              href="/archive",
            ),

            A(
              Div(
                Img(src='/svg/ytc-1.svg', cls='w-full h-full group-hover:hide group-hover:opacity-0 transform rotate-1 transition-all ease-in-out'),
                Img(src='/svg/ytc-2.svg', cls='w-full h-full absolute top-0 left-0 opacity-0 group-hover:opacity-100 transform transition-all ease-in-out rotate-7'),
                cls='group relative items-center w-full h-full',
              ),
              href="/ytc/sepine",
              cls='block w-4/5 mx-auto my-8 relative',
            ),

            A(
              Div(
                Img(src='/svg/datura-1.svg', cls='w-full h-full group-hover:hide group-hover:opacity-0 transform transition-all ease-in-out'),
                Img(src='/svg/datura-2.svg', cls='w-full h-full absolute top-0 left-0 opacity-0 transition-all group-hover:opacity-100 transform scale-100 ease-in-out'),
                cls='group relative flex flex-col items-center w-full h-full',
              ),
              href='#',
              id="datura-mobile",
              cls='block w-4/5 mx-auto my-8 relative',
            ),

            A(
              Div(
                Img(src='/svg/sketch-dump-1.svg', cls='w-full h-full group-hover:hide group-hover:opacity-0 transform rotate-0 ease-in-out transition-all ease-in-out'),
                Img(src='/svg/sketch-dump-2.svg', cls='absolute top-0 left-0 w-full h-full opacity-0 group-hover:opacity-100 transform rotate-2 ease-in-out transition-all ease-in-out'),
                cls='group relative items-center w-full h-full',
              ),
              href='/sketchdump',
              cls='block w-4/5 mx-auto my-8 relative',
            ),

            A(
              Div(
                Img(src='/svg/grotto-goblins-1.svg', cls='w-full h-full group-hover:hide group-hover:opacity-0 transform rotate-3 ease-in-out transition-all ease-in-out'),
                Img(src='/svg/grotto-goblins-2.svg', cls='w-full h-full absolute top-0 left-0 opacity-0 duration-100 transition-all group-hover:opacity-100 transform rotate-7 ease-in-out'),
                cls='group relative items-center w-full h-full',
              ),
              href='#',
              cls='block w-4/5 mx-auto my-8 relative',
            ),
            cls='md:hidden flex flex-col min-h-screen py-16 px-4',
            id="mobile-grid",
          ),
        ),
      ),
      cls='relative',
    ),
  )
