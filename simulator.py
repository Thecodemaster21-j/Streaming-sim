# simulator.py
import requests
import time

def simulate_single_user(video_id):
    """Simulate one user watching a video, measure response time."""
    url = f"http://127.0.0.1:5000/video/{video_id}"
    
    # Measure time to first byte (TTFB) and total response time
    start = time.time()
    try:
        response = requests.get(url, timeout=5)
        ttfb = response.elapsed.total_seconds()  # time until first byte received
        total_time = time.time() - start
        
        print(f"Video {video_id}:")
        print(f"  Status: {response.status_code}")
        print(f"  TTFB: {ttfb:.3f}s")
        print(f"  Total time: {total_time:.3f}s")
        print(f"  Data size: {response.json().get('size_kb')} KB")
    except requests.exceptions.Timeout:
        print(f"Video {video_id}: Request timed out")
    except Exception as e:
        print(f"Video {video_id}: Error - {e}")

if __name__ == '__main__':
    # Simulate a single user requesting video with ID 1
    simulate_single_user(1)