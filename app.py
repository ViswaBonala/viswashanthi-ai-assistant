from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resume_context = """
Viswashanthi Bonala is an ETL Lead with 13+ years of experience.
She led offshore teams of 6–8 developers.
Owned production support and SLA adherence.
Contributed to ETL framework design including logging and restartability.
Migrated DB2/Mainframe to Snowflake.
Reduced ETL load time by 35%.
Implemented automated validation reducing defects by 70%.
Strong in SQL, Python, Informatica, Snowflake, GCP,  A/B Testing.
"""

@app.route("/chat", methods=["POST"])
def chat():
    user_question = request.json.get("question")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional AI assistant representing ETL Lead Viswashanthi Bonala. Respond concisely and professionally."},
            {"role": "user", "content": f"Context:\n{resume_context}\n\nQuestion:\n{user_question}"}
        ]
    )

    return jsonify({"answer": response.choices[0].message.content})

if __name__ == "__main__":
    app.run()