from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os

app = FastAPI()

DESTINATIONS = [
    "bali", "dubai", "maldives", "kashmir", "mauritius", "europe", "greece", 
    "switzerland", "russia", "ladakh", "himachal-pradesh", "uttarakhand", "spiti", 
    "rajasthan", "meghalaya", "sikkim", "andaman", "kerala", "goa", "coorg", 
    "arunachal-pradesh", "varanasi", "odisha", "vietnam", "thailand", "japan", 
    "sri-lanka", "philippines", "singapore", "malaysia", "turkey", "georgia", "bhutan"
]

@app.get("/")
async def index():
    return FileResponse("index.html")

@app.get("/honeymoon")
async def honeymoon():
    return FileResponse("experiences.html")

@app.get("/destinations")
async def destinations():
    return FileResponse("destinations.html")

@app.get("/about")
async def about():
    return FileResponse("about-us.html")

@app.get("/pay-us")
async def pay_us():
    return FileResponse("pay-us.html")

@app.get("/packages/{slug}")
async def packages(slug: str):
    matched = "mauritius" # default fallback
    for d in DESTINATIONS:
        if d in slug.lower():
            matched = d
            break
    file_path = f"destinations/{matched}.html"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return FileResponse("index.html")

@app.get("/{path:path}")
async def catch_all(request: Request, path: str):
    safe_path = os.path.normpath(path)
    if safe_path.startswith("..") or safe_path.startswith("/"):
        return FileResponse("404.html") if os.path.exists("404.html") else FileResponse("index.html")
        
    if os.path.exists(safe_path):
        if os.path.isdir(safe_path):
            idx = os.path.join(safe_path, "index.html")
            if os.path.exists(idx):
                return FileResponse(idx)
        else:
            return FileResponse(safe_path)
            
    html_path = f"{safe_path}.html"
    if os.path.exists(html_path):
        return FileResponse(html_path)
        
    return FileResponse("404.html") if os.path.exists("404.html") else FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    print("Serving at port 3000 with FastAPI...")
    uvicorn.run(app, host="0.0.0.0", port=3000)
