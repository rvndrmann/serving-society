#!/usr/bin/env python3
"""Serving Society — Generate all website images via fal.ai Nano Banana 2 (using curl)"""

import json, os, time, subprocess

FAL_KEY = "644df6fc-b68f-4f20-acf1-84c585b0bad7:8f70c52537846bf2b3ab9193e7c5404f"
API_URL = "https://queue.fal.run/fal-ai/nano-banana-2"
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(IMG_DIR, exist_ok=True)

SUFFIX = "Shot on 35mm, natural soft daylight, shallow depth of field, warm cinematic color grade, authentic candid expressions, photorealistic, 4k, Australian setting."

IMAGES = [
    ("hero-homepage", f"A diverse group photograph of an NDIS support worker smiling warmly alongside a person using a wheelchair in a sunlit Australian community park. Natural morning light, lens flare, soft bokeh of green trees in background. Support worker wears casual professional attire; participant looks confident and happy. Warm purple and golden tones. {SUFFIX}"),
    ("about-hero", f"Candid photo of a young male support worker and an older male participant in a wheelchair, sitting together outdoors in a sunny Australian park, reading a booklet together. Both smiling naturally, relaxed body language. Lush green grass and trees in soft bokeh background. Warm golden-hour light. {SUFFIX}"),
    ("about-vision", f"A female support worker assisting a young woman with disability at a laptop in a bright modern office space. Both focused on the screen, collaborative posture. Natural window light, indoor plants. Professional yet warm atmosphere. {SUFFIX}"),
    ("about-mission", f"A diverse group of adults with mixed abilities gathered around a table doing a creative art activity together, smiling and laughing. Bright community centre room, colourful supplies on the table. Warm, inclusive, joyful. {SUFFIX}"),
    ("accommodation-tenancy", f"A support worker helping a young adult participant review rental paperwork at a kitchen table in a bright modern Australian apartment. Both seated, relaxed, documents and a laptop visible. Warm natural light from a nearby window. Conveys security and independence. {SUFFIX}"),
    ("life-stage-transition", f"A candid outdoor photo of a young man with Down syndrome and his support worker walking together along a tree-lined suburban Australian street, both carrying shopping bags and laughing. Bright afternoon sun, shadows on the path. Conveys transition, independence, community. {SUFFIX}"),
    ("daily-tasks-shared-living", f"Two adults in a shared living kitchen, one stirring a pot on the stove while the other chops vegetables nearby. A friendly support worker observes and guides. Clean modern Australian kitchen, natural daylight, warm homey feel. {SUFFIX}"),
    ("development-life-skills", f"Close-up of hands counting Australian dollar notes on a wooden table with a budget planner, calculator, and a cup of tea. Soft natural light, shallow depth of field. Represents money management and practical life skill development. {SUFFIX}"),
    ("community-participation", f"Three people, one in a motorised wheelchair, enjoying a sunny day at a local Australian outdoor market. Colourful market stalls in background, all three smiling and engaged in conversation. Authentic street photography feel. {SUFFIX}"),
    ("assist-personal-activities", f"A female support worker gently helping a young woman brush her hair in a bright clean bathroom. Mirror reflection visible, warm lighting, dignified and respectful interaction. Focus on partnership not dependency. {SUFFIX}"),
    ("assist-travel-transport", f"A male support worker assisting a participant in a wheelchair entering an accessible van via a ramp, in a sunny Australian suburban driveway. Van door open, clear blue sky, green hedges. Conveys mobility, freedom, reliable support. {SUFFIX}"),
    ("innovative-community", f"A diverse group of young adults in an art studio, one painting on canvas, another working on pottery, a third at a digital tablet. Bright creative space with colourful artwork on walls. Energetic, inspiring, inclusive. {SUFFIX}"),
    ("household-tasks", f"A support worker and a participant folding laundry together on a couch in a bright tidy Australian living room. Both relaxed and smiling, sunlight streaming through curtains. Warm domestic scene, collaborative. {SUFFIX}"),
    ("appointment", f"A friendly female receptionist with a headset, sitting at a clean white desk, smiling while looking at her computer screen. Bright modern office, purple accent wall in background, small plant on desk. Welcoming, professional. {SUFFIX}"),
]

def curl_json(method, url, data=None):
    cmd = ["curl", "-s", "--request", method, "--url", url,
           "--header", f"Authorization: Key {FAL_KEY}",
           "--header", "Content-Type: application/json"]
    if data:
        cmd += ["--data", json.dumps(data)]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout)

def download(url, path):
    subprocess.run(["curl", "-s", "-o", path, url], timeout=60)

def generate(name, prompt):
    out = os.path.join(IMG_DIR, f"{name}.png")
    if os.path.exists(out):
        print(f"  SKIP  {name}")
        return True

    print(f"  SEND  {name}")
    resp = curl_json("POST", API_URL, {
        "prompt": prompt,
        "num_images": 1,
        "aspect_ratio": "16:9",
        "output_format": "png",
        "safety_tolerance": "5",
        "resolution": "1K",
        "limit_generations": True,
    })
    rid = resp.get("request_id")
    if not rid:
        print(f"  FAIL  {name}: {resp}")
        return False

    for i in range(90):
        time.sleep(3)
        sr = curl_json("GET", f"{API_URL}/requests/{rid}/status")
        st = sr.get("status", "?")
        print(f"         [{i+1}] {st}")
        if st == "COMPLETED":
            break
        if st == "FAILED":
            print(f"  FAIL  {name}")
            return False
    else:
        print(f"  TIMEOUT  {name}")
        return False

    result = curl_json("GET", f"{API_URL}/requests/{rid}")
    url = result["images"][0]["url"]
    download(url, out)
    kb = os.path.getsize(out) // 1024
    print(f"  DONE  {name} ({kb} KB)")
    return True

if __name__ == "__main__":
    print(f"\n{'='*50}")
    print(f"  Serving Society — Image Generation")
    print(f"  {len(IMAGES)} images to generate")
    print(f"{'='*50}\n")

    ok = fail = 0
    for name, prompt in IMAGES:
        try:
            if generate(name, prompt):
                ok += 1
            else:
                fail += 1
        except Exception as e:
            print(f"  ERROR {name}: {e}")
            fail += 1
        print()

    print(f"{'='*50}")
    print(f"  Results: {ok} success, {fail} failed")
    print(f"  Images in: {IMG_DIR}")
    print(f"{'='*50}")
