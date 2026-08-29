from fastapi import FastAPI

app = FastAPI(
    title="Recommendation System API",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "ok", "model": "hybrid_recommendation_engine"}

# Recommendation serving functions will be wired here
# from the saved artifacts in the final backend package.
