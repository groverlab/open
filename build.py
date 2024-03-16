
projects = [
    {
        "name": "Pneumatic error detector",
        "img": "error_detector.jpeg",
        "links": [("arXiv", "https://arxiv.org/abs/2401.16500")]
    },
    {
        "name": "Pressurama",
        "img": "error_detector.jpeg",
        "links": [("GitHub", "https://github.com/groverlab/pressurama")]
    },
    {
        "name": "Vacuum-powered Intermittent Pneumatic Compression (IPC) device",
        "img": "error_detector.jpeg",
        "links": [("arXiv", "https://arxiv.org/abs/2401.16500")]
    }
]


infile1 = open("1.html", "r")
infile2 = open("2.html", "r")
outfile = open("index.html", "w")

outfile.write(infile1.read())
for p in projects:
    outfile.write('<div class="col"><div class="card shadow-sm">')
    outfile.write(f'<img src="assets/{p["img"]}">')
    outfile.write('<div class="card-body">')
    outfile.write(f'<p class="card-text">{p["name"]}</p>')
    outfile.write('<div class="d-flex justify-content-between align-items-center"><div class="btn-group">')
    for link in p["links"]:
        outfile.write(f'<a href="{link[1]}">')
        outfile.write(f'<button type="button" class="btn btn-sm btn-outline-secondary">{link[0]}</button>')
        outfile.write('</a></div></div></div></div></div>')

outfile.write(infile2.read())
outfile.close()
print("DONE")