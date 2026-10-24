from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
)


def get_client():
    return client