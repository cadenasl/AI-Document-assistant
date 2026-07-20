from services.ai.ollama_service import get_client
from services.ai.prompts import DOCUMENT_ANALYSIS_PROMPT,DOCUMENT_QA_PROMPT


class DocumentAnalyzer:

    def __init__(self):
        self.client = get_client()
        self.model = "llama3.2:3b"

    def answer_question(self, question: str, chunks: list[str]):
        context = "\n\n".join(chunks)
        prompt = f"""
        Context:
        {context}

        Question:
        {question}
        """

        return self._generate(
            DOCUMENT_QA_PROMPT,
            prompt,
        )
    def summarize(self, chunks: list[str]):
            text="\n\n".join(chunks)
            return self._generate(
            DOCUMENT_ANALYSIS_PROMPT,
            text,
             )
   
    def _generate(self, system_prompt: str, user_prompt: str):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )
        return response.choices[0].message.content