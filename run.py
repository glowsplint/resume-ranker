import uvicorn

if __name__ == '__main__':
    uvicorn.run('resumeranker:app', host='127.0.0.1', port=5000,
                reload=True, debug=True, workers=1)
