import gradio as gr
from query import ask


def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)

    sources = "\n".join(f"• {source}" for source in result["sources"])

    return result["answer"], sources


with gr.Blocks(title="USF Off-Campus Housing Guide") as demo:
    gr.Markdown("# The Unofficial Guide: USF Off-Campus Housing")
    gr.Markdown("Ask questions based on collected apartment reviews near USF.")

    question = gr.Textbox(
        label="Your question",
        placeholder="Example: What do residents say about maintenance at Avalon Heights?",
        lines=2,
    )

    ask_button = gr.Button("Ask")

    answer = gr.Textbox(label="Answer", lines=10)
    sources = gr.Textbox(label="Retrieved Sources", lines=6)

    ask_button.click(handle_query, inputs=question, outputs=[answer, sources])
    question.submit(handle_query, inputs=question, outputs=[answer, sources])


if __name__ == "__main__":
    demo.launch()