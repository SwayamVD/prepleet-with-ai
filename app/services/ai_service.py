import google.generativeai as genai
genai.configure(api_key="AIzaSyBPurTgr1YTZgAsNNvjgC2G_ZgirEwS4OQ")
import re,json


# return analysis about the complete program<code>
def gen_analysis(data):
    code = data.get("code", "")
    language = data.get("language", "unknown")
    idtitle = "Leetcode Question: " + data.get("idtitle")
    prompt = """
            Analyze the Python code below, which is a solution to a LeetCode problem. The code may be a standalone function.
            1) Return a JSON object with keys:
            - verify: if you found any mistakes (logical, syntax, or didnt satify the leetcode question description) alert or else just say Correct Code.
            - time_complexity: {best, average, worst} (Big-O strings) -give short reason why
            - space_complexity: string (Big-O) -give short reason why
            - explanation: step-by-step explanation (short)
            - optimization_suggestions: bullet list (short)
            - refactored_code: code (if applicable)

            2) ONLY return valid JSON (no extra text).
        """
    full_prompt = f"{idtitle}\n{prompt}\n\nLanguage: {language}\n\nCode:\n{code}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(full_prompt)
    raw_text = response.text.strip()

    cleaned = re.sub(r"^```json\s*|\s*```$", "", raw_text, flags=re.DOTALL).strip()

    try:
        parsed_json = json.loads(cleaned)
    except Exception as e:
        parsed_json = {
            "error": f"Failed to parse JSON: {str(e)}",
            "raw_output": raw_text
        }

    return parsed_json  

# return recomendation or hints when user stucks during solving
def gen_hints(data):
    code = data.get("code", "")
    language = data.get("language", "unknown")
    idtitle = data.get("idtitle")


    prompt=f"""
        I am stuck while solving a programming problem.
        I am solving a leetcode problem {idtitle}
        Please analyze what I am trying to do, identify any misconceptions, and guide me with the correct approach to solve the problem.
        Do not give the full solution.
        Explain the key concept(s) I need to understand in very short, simple terms.
        Focus on helping me learn and think through the problem, not just giving the answer.


        ONLY return valid JSON (no extra text) with following fields.
        - analysis: analyze the code and tell the vulnerability or find where he went wrong
        - keyconcepts: suggest one concept that i can help the user , explain in short how to implement it.
        """



    full_prompt = f"{prompt}\n\nLanguage: {language}\n\nCode:\n{code}"


    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(full_prompt)
    raw_text = response.text.strip()

    cleaned = re.sub(r"^```json\s*|\s*```$", "", raw_text, flags=re.DOTALL).strip()
    print(cleaned)
    try:
        parsed_json = json.loads(cleaned)
    except Exception as e:
        parsed_json = {
            "error": f"Failed to parse JSON: {str(e)}",
            "raw_output": raw_text
        }

    return parsed_json
