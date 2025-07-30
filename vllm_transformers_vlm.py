import requests
from PIL import Image
from transformers import AutoProcessor
from vllm import LLM, SamplingParams

model_id = "llava-hf/llava-onevision-qwen2-0.5b-ov-hf"
image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"

processor = AutoProcessor.from_pretrained(model_id)
image = Image.open(requests.get(image_url, stream=True).raw)

messages = [{
    "role": "user",
    "content": [
        {"type": "image", "url": "dummy_image.jpg"},
        {"type": "text", "text": "What is the content of this image?"}
    ],
}]
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Run model
vlm = LLM(model=model_id, model_impl="transformers")
outputs = vlm.generate(
    {"prompt": prompt, "multi_modal_data": {"image": image}},
    sampling_params=SamplingParams(max_tokens=100),
)

print(outputs[0].outputs[0].text)

