import google.generativeai as genai


genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_skills(cv_text: str):
    try:
        prompt = f"""
        You are a strict JSON generator.

        Extract CV information and return ONLY valid JSON.

        RULES:
        - No markdown
        - No ``` fences
        - No explanation
        - No null values (use empty arrays or empty strings instead)

        FORMAT:
        {{
        "skills": [],
        "experience_summary": "",
        "suggestions": []
        }}

        TEXT:
        {cv_text}
        """

        response = model.generate_content(prompt)

        # SAFE return
        return response.text

    except Exception as e:
        return {"error": str(e)}