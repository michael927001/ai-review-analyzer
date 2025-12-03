from fastapi import FastAPI, UploadFile, File
import csv
import io

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Review Analyzer API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/upload")
async def upload_reviews(file: UploadFile = File(...)):
    contents = await file.read()
    text_stream = io.StringIO(contents.decode("utf-8"))
    reader = csv.reader(text_stream)

    reviews = []
    for row in reader:
        if len(row) > 0:
            reviews.append(row[0])

    return {
        "total_reviews": len(reviews),
        "sample": reviews[:3]  # Show first 3 reviews
    }
