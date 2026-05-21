import os
import base64
import typing
from openai import OpenAI
from gradio import Server
from gradio.data_classes import FileData
from fastapi.responses import HTMLResponse

app = Server()

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="fw_VmqyWZdPK5BtU32b6YfWCN",
# client = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=os.environ.get("HF_TOKEN", ""),
    default_headers={
        "X-HF-Bill-To": "huggingface"
    }
)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

@app.api()
def chat(message: str, history: typing.List[typing.List[str]], image: typing.Optional[FileData] = None) -> str:
    system_prompt = """You are Kimi K2.6, a large language model trained by Moonshot AI.

1. Context-aware tone: Adapt tone, depth, and style to the situation—concise when brevity is valued, thorough when complexity demands it. Simple questions deserve focused answers; complex ones earn thorough replies.
2. Readable flow: Organize longer answers with clear section headings. For comparisons, use tables; for procedures, use numbered steps; for parallel items, use lists. Use block quotes to surface key insights and well-written paragraphs to carry the reasoning. Use selective highlights to guide the eye.
1"""

    messages = [{"role": "system", "content": system_prompt}]
    
    # Reconstruct history
    for user_msg, assistant_msg in history:
        if user_msg:
            messages.append({"role": "user", "content": [{"type": "text", "text": user_msg}]})
        if assistant_msg:
            messages.append({"role": "assistant", "content": [{"type": "text", "text": assistant_msg}]})
            
    # Add new message
    content = []
    if message:
        content.append({"type": "text", "text": message})
    else:
        if image:
            content.append({"type": "text", "text": "Describe this image."})
            
    if image:
        base64_image = encode_image(image.path)
        img_type = "image/png"
        if image.path.lower().endswith("jpg") or image.path.lower().endswith("jpeg"):
            img_type = "image/jpeg"
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:{img_type};base64,{base64_image}"
            }
        })
        
    messages.append({
        "role": "user",
        "content": content
    })
        
    try:
        completion = client.chat.completions.create(
            model="accounts/fireworks/models/kimi-k2p6",
            # model="moonshotai/Kimi-K2.6:fireworks-ai",
            messages=messages,
            stream=False
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

@app.get("/")
async def homepage():
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

if __name__ == "__main__":
    app.launch()
