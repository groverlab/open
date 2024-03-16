infile1 = open("1.html", "r")
infile2 = open("2.html", "r")
outfile = open("index.html", "w")

outfile.write(infile1.read())
for _ in range(10):
    outfile.write("""

        
        <div class="col">
          <div class="card shadow-sm">
            <img src="assets/error_detector.jpeg">
            <div class="card-body">
              <p class="card-text">Pneumatic error detector</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <a href="https://arxiv.org/abs/2401.16500">
                    <button type="button" class="btn btn-sm btn-outline-secondary">arXiv</button>
                  </a>
                </div>
                <!-- <small class="text-body-secondary">Design in Adobe Illustrator and SVG</small> -->
              </div>
            </div>
          </div>
        </div>


    """)

outfile.write(infile2.read())
outfile.close()
print("DONE")