# Racconbot's functional enhancement
Enhancing Raccoonbot's ability

## Project Overview.
Extending RaccoonBot pipeline by adding multiple objects, tasks, and instructions while improving OpenVLA action mapping and adding YOLO for real robot

## Extension

### New objects
- Color : red, blue, green, yellow
- Shape: cylinder, cube, sphere, box

### New instrusctions
- grasp : "pick up the {color} cylinder"
- lift : "raise up the {color} cylinder"
- push : "move the {color} cylinder forward"
- pick-and-place : "pick up the {color} cylinder and place it"
- stack : "place the {color} cylinder on top of another"
- swap : "switch the {color} cylinder position"

### Dataset
- 400 MuJoco demonstration generated
- RLDS/TFDS rebuild
- LoRa fine-tuned

## Imporvement

### 7D-to-$DOF ACtion Mapping
- max_delta_xyz :: 0.01 -> 0.015
- delta_scale : 1.0 -> 1.2
- max_retries : 3 -> 5
- Effect : make it faster and more reliable robot motion

### Timing Log
- Added [TIMING] inference_time log to openvla_server.py
- Inference time : 0.21~0.27s per step

## Additional

### YOLO Webcam Color Detection
- Dectet target color from webcam using color range
- Automatically chooses target color based on detected color

### Limitation
- Sim to Real gap : Real robot moves based on OpenVla, not using camera
- Future work : set real environment based on the camera

## How to Run

### Server
```bash
cd openvla && python openvla_server.py \
  --model_path openvla-runs/openvla-7b-finetuned-raccoonbot \
  --default-unnorm-key raccoon_pick_place \
  --host 0.0.0.0 --port 8000 --device cuda
```

### Client - Simulation
```bash
python openvla_multicolor_client.py \
  --server_url https://YOUR_TUNNEL_URL \
  --xml_path Raccoon_colored_cylinder.xml \
  --target_color red --use_viewer
```

### Client - Real Robot + YOLO
```bash
python openvla_multicolor_client_real_robot.py \
  --server_url https://YOUR_TUNNEL_URL \
  --target_color red --use_real_robot --use_viewer
```
