from fastapi import FastAPI, UploadFile, File
import fitz
from gemini import extract_skills
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "CareerForgeAI backend is running 🚀"}


@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):

    contents = await file.read()

    # save file
    with open("temp.pdf", "wb") as f:
        f.write(contents)

    # extract text
    doc = fitz.open("temp.pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    # 🔥 SEND TO GEMINI HERE
    ai_result = extract_skills(text)

    return {
        "filename": file.filename,
        "ai_analysis": ai_result if ai_result else "No AI output"
    }