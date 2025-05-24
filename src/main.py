from fasthtml.common import *

from pages.archive.archive import archive
from pages.archive.sb1 import sb1
from pages.archive.sb2 import sb2
from pages.archive.sb3 import sb3
from pages.archive.sb4 import sb4
from pages.archive.sb5 import sb5
from pages.index import index
from pages.sketchdump import sketchdump
from pages.ytc.sepine import sepine
from pages.ytc.sepine_caves import sepine_caves
from pages.ytc.sepine_forest import sepine_forest
from pages.ytc.sepine_sore import sepine_shoreline

app = FastHTML(surreal=True, pico=False, htmx=False, hdrs=Link(rel="stylesheet", href="/app.css", type="text/css"))

app.route("/")(index)

app.route("/archive")(archive)
app.route("/archive/sb1")(sb1)
app.route("/archive/sb2")(sb2)
app.route("/archive/sb3")(sb3)
app.route("/archive/sb4")(sb4)
app.route("/archive/sb5")(sb5)

app.route("/sketchdump")(sketchdump)

app.route("/ytc/sepine")(sepine)
app.route("/ytc/sepine/sepine_caves")(sepine_caves)
app.route("/ytc/sepine/sepine_forest")(sepine_forest)
app.route("/ytc/sepine/sepine_shoreline")(sepine_shoreline)

@app.get("/{fname:path}.{ext:static}")
def serve_files(fname: str, ext: str):
  @flexicache()
  def f(fname: str, ext: str):
    return FileResponse(f'public/{fname}.{ext}')
  return f(fname, ext)

serve(reload=False)
