from fastapi import FastAPI, HTTPException, status
from preprocessing.property_input import PropertyInput
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

# Define the FastAPI app instance
app = FastAPI()


# Request returning "alive" if the server is alive.
@app.get("/")
async def root():
    return {"message": "alive"}


# Request returning a string to explain what the POST expect (data and format).
@app.get("/predict")
async def predict_get():
    # TODO: update the message
    return {"message": "We have to put in here the explanation of what the POST expect"}


# Request that receives the data of a house in JSON format.
@app.post("/predict")
async def predict_post(data: PropertyInput):
    try:
        # TODO: handle exceptions/errors
        df = preprocess(data)
        predicted_price = predict(df)

        return {"prediction": predicted_price, "status_code": status.HTTP_200_OK}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
