
projectsfile = open("projects.txt", "r")
infile1 = open("1.html", "r")
infile2 = open("2.html", "r")
outfile = open("index.html", "w")

outfile.write(infile1.read())
for project in projectsfile.read().split("\n\n"):
    name, image, *links = project.split("\n")
    outfile.write('<div class="col"><div class="card shadow-sm">')
    outfile.write(f'<img src="assets/{image}">')
    outfile.write('<div class="card-body">')
    outfile.write(f'<p class="card-text">{name}</p>')
    outfile.write('<div class="d-flex justify-content-between align-items-center"><div class="btn-group">')
    for link in links:
        outfile.write(f'<a href="{link.split()[1]}">')
        outfile.write(f'<button type="button" class="btn btn-sm btn-outline-secondary">{link.split()[0]}</button>')
    outfile.write('</a></div></div></div></div></div>')

outfile.write(infile2.read())
outfile.close()
print("DONE")