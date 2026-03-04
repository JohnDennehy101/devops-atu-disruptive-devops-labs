from fastapi import FastAPI

app = FastAPI(
    title="Simple API for Documentation Lab",
    description="A proof of concept for automated Swagger/OpenAPI docs",
    version="1.0.0"
)

# Sample endpoint one
@app.get("/one", tags=["Main Features"], summary="Fetch message one")
def first():
    """
    Description for first endpoint
    """
    
    return {"message": "This is the first endpoint"}

# Sample endpoint two
@app.get("/two", tags=["Secondary Features"], summary="Fetch message two")
def second():
    """
    Description for second endpoint
    """

    return {"message": "This is the second endpoint"}