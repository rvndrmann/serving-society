#!/bin/bash
# Serving Society — Image Generator using fal.ai Nano Banana 2
# Usage: bash generate_images.sh

export FAL_KEY="644df6fc-b68f-4f20-acf1-84c585b0bad7:8f70c52537846bf2b3ab9193e7c5404f"
API_URL="https://queue.fal.run/fal-ai/nano-banana-2"
IMG_DIR="$(cd "$(dirname "$0")" && pwd)/images"
mkdir -p "$IMG_DIR"

# ── Image prompts ──
declare -A PROMPTS

PROMPTS["hero-homepage"]="A diverse group photograph of an NDIS support worker smiling warmly alongside a person using a wheelchair in a sunlit Australian community park. Natural morning light, lens flare, soft bokeh of green trees in background. Support worker wears casual professional attire; participant looks confident and happy. Warm purple and golden tones. Shot on 35mm, shallow depth of field, photorealistic, 4k."

PROMPTS["about-hero"]="Candid photo of a young male support worker and an older male participant in a wheelchair, sitting together outdoors in a sunny Australian park, reading a booklet together. Both smiling naturally, relaxed body language. Lush green grass and trees in soft bokeh background. Warm golden-hour light. Shot on 35mm, photorealistic, 4k."

PROMPTS["about-vision"]="A female support worker assisting a young woman with disability at a laptop in a bright modern office space. Both focused on the screen, collaborative posture. Natural window light, indoor plants. Professional yet warm atmosphere. Shot on 35mm, photorealistic, 4k, Australian setting."

PROMPTS["about-mission"]="A diverse group of adults with mixed abilities gathered around a table doing a creative art activity together, smiling and laughing. Bright community centre room, colourful supplies on the table. Warm, inclusive, joyful. Shot on 35mm, photorealistic, 4k."

PROMPTS["accommodation-tenancy"]="A support worker helping a young adult participant review rental paperwork at a kitchen table in a bright modern Australian apartment. Both seated, relaxed, documents and a laptop visible. Warm natural light from a nearby window. Conveys security and independence. Shot on 35mm, photorealistic, 4k."

PROMPTS["life-stage-transition"]="A candid outdoor photo of a young man with Down syndrome and his support worker walking together along a tree-lined suburban Australian street, both carrying shopping bags and laughing. Bright afternoon sun, shadows on the path. Conveys transition, independence, community. Shot on 35mm, photorealistic, 4k."

PROMPTS["daily-tasks-shared-living"]="Two adults in a shared living kitchen — one stirring a pot on the stove while the other chops vegetables nearby. A friendly support worker observes and guides. Clean modern Australian kitchen, natural daylight, warm homey feel. Shot on 35mm, photorealistic, 4k."

PROMPTS["development-life-skills"]="Close-up of hands counting Australian dollar notes on a wooden table with a budget planner, calculator, and a cup of tea. Soft natural light, shallow depth of field. Represents money management and practical life skill development. Shot on 35mm, photorealistic, 4k."

PROMPTS["community-participation"]="Three people — one in a motorised wheelchair — enjoying a sunny day at a local Australian outdoor market. Colourful market stalls in background, all three smiling and engaged in conversation. Authentic street photography feel. Shot on 35mm, photorealistic, 4k."

PROMPTS["assist-personal-activities"]="A female support worker gently helping a young woman brush her hair in a bright clean bathroom. Mirror reflection visible, warm lighting, dignified and respectful interaction. Focus on partnership not dependency. Shot on 35mm, photorealistic, 4k, Australian setting."

PROMPTS["assist-travel-transport"]="A male support worker assisting a participant in a wheelchair entering an accessible van via a ramp, in a sunny Australian suburban driveway. Van door open, clear blue sky, green hedges. Conveys mobility, freedom, reliable support. Shot on 35mm, photorealistic, 4k."

PROMPTS["innovative-community"]="A diverse group of young adults in an art studio — one painting on canvas, another working on pottery, a third at a digital tablet. Bright creative space with colourful artwork on walls. Energetic, inspiring, inclusive. Shot on 35mm, photorealistic, 4k."

PROMPTS["household-tasks"]="A support worker and a participant folding laundry together on a couch in a bright tidy Australian living room. Both relaxed and smiling, sunlight streaming through curtains. Warm domestic scene, collaborative. Shot on 35mm, photorealistic, 4k."

PROMPTS["appointment"]="A friendly female receptionist with a headset, sitting at a clean white desk, smiling while looking at her computer screen. Bright modern office, purple accent wall in background, small plant on desk. Welcoming, professional. Shot on 35mm, photorealistic, 4k."

# ── Generate function ──
generate_image() {
  local name="$1"
  local prompt="$2"
  local output_file="$IMG_DIR/${name}.png"

  if [ -f "$output_file" ]; then
    echo "⏭  $name — already exists, skipping"
    return 0
  fi

  echo "🚀 Submitting: $name"

  # Submit request
  local response
  response=$(curl -s --request POST \
    --url "$API_URL" \
    --header "Authorization: Key $FAL_KEY" \
    --header "Content-Type: application/json" \
    --data "$(cat <<EOF
{
  "prompt": $(echo "$prompt" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().strip()))'),
  "num_images": 1,
  "aspect_ratio": "16:9",
  "output_format": "png",
  "safety_tolerance": "5",
  "resolution": "1K",
  "limit_generations": true
}
EOF
)")

  local request_id
  request_id=$(echo "$response" | python3 -c "import json,sys; print(json.load(sys.stdin).get('request_id',''))" 2>/dev/null)

  if [ -z "$request_id" ]; then
    echo "❌ $name — failed to submit. Response: $response"
    return 1
  fi

  echo "   Request ID: $request_id"

  # Poll for completion
  local status="IN_QUEUE"
  local attempts=0
  while [ "$status" != "COMPLETED" ] && [ "$attempts" -lt 60 ]; do
    sleep 3
    local status_response
    status_response=$(curl -s --request GET \
      --url "$API_URL/requests/$request_id/status" \
      --header "Authorization: Key $FAL_KEY")
    status=$(echo "$status_response" | python3 -c "import json,sys; print(json.load(sys.stdin).get('status','UNKNOWN'))" 2>/dev/null)
    attempts=$((attempts + 1))
    echo "   [$attempts] Status: $status"

    if [ "$status" = "FAILED" ]; then
      echo "❌ $name — generation failed"
      return 1
    fi
  done

  if [ "$status" != "COMPLETED" ]; then
    echo "❌ $name — timed out"
    return 1
  fi

  # Fetch result
  local result
  result=$(curl -s --request GET \
    --url "$API_URL/requests/$request_id" \
    --header "Authorization: Key $FAL_KEY")

  local image_url
  image_url=$(echo "$result" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['images'][0]['url'])" 2>/dev/null)

  if [ -z "$image_url" ]; then
    echo "❌ $name — no image URL in result"
    return 1
  fi

  # Download
  curl -s -o "$output_file" "$image_url"
  echo "✅ $name — saved to $output_file"
}

# ── Run all ──
echo "================================================"
echo "  Serving Society — Image Generation"
echo "  ${#PROMPTS[@]} images to generate"
echo "================================================"
echo ""

for name in "${!PROMPTS[@]}"; do
  generate_image "$name" "${PROMPTS[$name]}"
  echo ""
done

echo "================================================"
echo "  Done! Images saved to: $IMG_DIR"
echo "================================================"
ls -la "$IMG_DIR"
