import uvicorn

if __name__ == "__main__":
    uvicorn.run("e_commerce_app.app:app",host='0.0.0.0', port=4557, reload=True, debug=True, workers=3)