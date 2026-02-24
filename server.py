# server.py
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

# Simulate a video streaming endpoint
@app.route('/video/<int:video_id>')
def stream_video(video_id):
    # Record start time for logging
    start_time = time.time()
    
    # Simulate network latency and video processing (e.g., 0.5-2 sec delay)
    delay = random.uniform(0.5, 2.0)
    time.sleep(delay)
    
    # Simulate video data (a large string)
    # In a real scenario, you'd stream chunks, but for now just return a dummy payload
    video_data = "X" * 1024 * 100  # 100 KB of dummy data
    
    end_time = time.time()
    processing_time = end_time - start_time
    
    # Log the request details (you can later write to a file)
    print(f"Video {video_id} served in {processing_time:.2f}s (delay: {delay:.2f}s)")
    
    return jsonify({
        "video_id": video_id,
        "size_kb": len(video_data) / 1024,
        "processing_time": processing_time
    })

if __name__ == '__main__':
    app.run(debug=True, threaded=True)   # threaded=True allows handling multiple requests