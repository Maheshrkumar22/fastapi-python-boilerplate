from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from url_scrape_data import scrape_data
import json
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("public/favicon.ico")


@app.get("/api/data")
def get_sample_data():
    return {
        "data": [
            {"id": 1, "name": "Sample Item 1", "value": 100},
            {"id": 2, "name": "Sample Item 2", "value": 200},
            {"id": 3, "name": "Sample Item 3", "value": 300}
        ],
        "total": 3,
        "timestamp": "2024-01-01T00:00:00Z"
    }


@app.get("/api/items/{item_id}")
def get_item(item_id: int):
    return {
        "item": {
            "id": item_id,
            "name": "Sample Item " + str(item_id),
            "value": item_id * 100
        },
        "timestamp": "2024-01-01T00:00:00Z"
    }
def process(url_name):

    results_json_string = scrape_data(url_name)
    # Parse the JSON string back into a Python list/dictionary
    results_list = json.loads(results_json_string)
    return results_list

@app.get("/api/{url_name:path}")
def read_item(url_name: str):
    try:
        df=pd.read_csv('data_pipeline.csv',delimiter=';')
        matched_row = df[df['url'].apply(lambda x: x in str(url_name).strip())]
        print("df loaded")

        if not matched_row.empty:
            response = matched_row.iloc[0]['response_json']
            print(f'pipeline response : {response}')
            #cleaned_string = response.encode('utf-8').decode('unicode_escape')

    # Step 3: Convert to Python list/dict
            data_json = json.loads(response)
            print(f'pipeline json response : {data_json}')

            # Step 4: Return as JSONResponse
            return JSONResponse(content=data_json)
            
        else:
            results_json = process(url_name)
            return results_json
        
    except Exception as e:  
        print(e)  
        data = [{
            "Name":"Data Not Found",
            "Designation":"Bot been blocked",
            "img url":None
            }]
        return JSONResponse(content=data)
