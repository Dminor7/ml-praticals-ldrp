import uvicorn

if __name__ == "__main__":
    uvicorn.run("e_commerce_app.app:app",host='0.0.0.0', port=4557, reload=True, debug=True, workers=3)

# import numpy as np
# import pandas as pd
# import joblib


# model = joblib.load("/home/darsh/workspace/ml-practicals-ldrp/e_commerce/e_commerce_app/e_commerce_app/models/lgbm_model.pkl")
# # np.array([12,3,4,1,3,64,15,4])

# # revenue = model.predict(np.array([[12,3,4,1,3,64,15,4,6,11]]))
# values = pd.Series([12,3,4,1,3,64,15,4,6,11]).astype("float64")
# revenue = model.predict(values,predict_disable_shape_check=True)

# print(revenue)