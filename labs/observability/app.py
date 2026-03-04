from fastapi import FastAPI
from prometheus_client import Counter, Histogram, make_asgi_app
import time
import random

app = FastAPI()

# Configure Prometheus tracking for number of requests
REQUEST_COUNT = Counter(
    "app_requests_total", 
    "Total HTTP Requests", 
    ["method", "endpoint", "http_status"]
)

# Configure Prometheus tracking for request latency
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds", 
    "Time spent processing request",
    ["endpoint"]
)

# /metrics endpoint which Prometheus scrapes to get the metrics data
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Sample endpoint to simulate a normal response for testing request counting and latency tracking
@app.get("/")
def home():
    start_time = time.time()
    
    # Random delay between 100ms and 500ms to simulate processing time
    time.sleep(random.uniform(0.1, 0.5))
    
    REQUEST_COUNT.labels(method="GET", endpoint="/", http_status=200).inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start_time)
    return {"message": "This is a normal response endpoint"}

# Sample endpoint to simulate a slower response for testing latency tracking
@app.get("/slow")
def slow_route():
    start_time = time.time()
    
    # Simulate a slow endpoint with a random delay between 1 and 2 seconds
    time.sleep(random.uniform(1.0, 2.0))
    
    REQUEST_COUNT.labels(method="GET", endpoint="/slow", http_status=200).inc()
    REQUEST_LATENCY.labels(endpoint="/slow").observe(time.time() - start_time)
    return {"message": "This is a slow response endpoint"}