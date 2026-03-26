from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools_setup import tools
from report_generator import format_report

load_dotenv()

llm = ChatOpenAI()

topic = input("Enter research topic: ")

web_result = tools[0].run(topic)
wiki_result = tools[1].run(topic)

combined = web_result + "\n" + wiki_result

prompt = f"Generate structured research report on {topic}: {combined}"

result = llm.invoke(prompt)

final_report = format_report(topic, result.content)

with open("research_report.txt", "w", encoding="utf-8") as f:
    f.write(final_report)

print(final_report)