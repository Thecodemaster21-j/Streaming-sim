from flask import Flask, request, jsonify
import time
import random 

app = Flask(__name__)

#  Video Streaming endpoint
@app.route('/stream', methods=['GET'])
def stream_video():
  start_time = time.time()

  delay = random.uniform(0.5, 2.0)  # Simulate variable processing time
  time.sleep(delay)


video_date = 'X' * 1024 * 100 

end_time = time.time()
processing_time = end_time - start_time

print(f'Video {video_id} served in {processing_time:.2f} seconds (delay: {delay:.2f} seconds)')
  return jsonify({
    'video_id': video_id,
    'processing_time': processing_time,
    'delay': delay
  })

if __name__ == '__main__':
  app.run(debug=True, threaded=True)