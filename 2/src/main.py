from fastapi import FastAPI, Query

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
async def filter_values(
    min: int = Query(0, ge=0),  
    max: int = Query(100, le=100) 
):
    if min > max:
        raise HTTPException(status_code=422, detail="min must be less than or equal to max")
    
    return {"min": min, "max": max}
# END
